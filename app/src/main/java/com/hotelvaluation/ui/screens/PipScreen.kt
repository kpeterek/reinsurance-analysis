package com.hotelvaluation.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.HotelValuationViewModel
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PipScreen(
    inputs: HotelInputs,
    result: ValuationResult,
    vm: HotelValuationViewModel,
    onBack: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Burgundy900),
    ) {
        TopAppBar(
            title = { Text("Property Improvement Plan") },
            navigationIcon = {
                IconButton(onClick = onBack) {
                    Icon(Icons.Filled.ArrowBack, "Back", tint = RoseGold)
                }
            },
            colors = TopAppBarDefaults.topAppBarColors(
                containerColor = Burgundy800,
                titleContentColor = IvoryWhite,
            ),
        )

        LiveValueBanner(result)

        Column(
            modifier = Modifier
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
        ) {
            ValuationCard(title = "PIP Configuration") {
                LabeledSwitch(
                    label = "Enable PIP Analysis",
                    checked = inputs.pipEnabled,
                    onCheckedChange = { vm.setPipEnabled(it) },
                )

                if (inputs.pipEnabled) {
                    Spacer(modifier = Modifier.height(8.dp))

                    InputRow(
                        label = "Total PIP Budget",
                        value = inputs.pipTotalCost.toDollarInput(),
                        onValueChange = { vm.setPipTotalCost(it.toDoubleOrDefault()) },
                        prefix = "$",
                    )
                    InputRow(
                        label = "Year 1 Spend (%)",
                        value = inputs.pipYear1Pct.toPctInput(),
                        onValueChange = { vm.setPipYear1Pct(it.fromPctInput()) },
                        isPercentage = true,
                    )

                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        "Year 2 Spend: ${Fmt.pct(inputs.pipYear2Pct)}",
                        style = MaterialTheme.typography.bodySmall,
                    )
                }
            }

            if (inputs.pipEnabled) {
                Spacer(modifier = Modifier.height(16.dp))

                ValuationCard(title = "Revenue Impact") {
                    InputRow(
                        label = "Year 1 Revenue Disruption",
                        value = inputs.pipRevenueDisruptionYear1.toPctInput(),
                        onValueChange = { vm.setPipRevenueDisruptionYear1(it.fromPctInput()) },
                        isPercentage = true,
                    )
                    InputRow(
                        label = "Year 2 Revenue Disruption",
                        value = inputs.pipRevenueDisruptionYear2.toPctInput(),
                        onValueChange = { vm.setPipRevenueDisruptionYear2(it.fromPctInput()) },
                        isPercentage = true,
                    )
                }

                Spacer(modifier = Modifier.height(16.dp))

                ValuationCard(title = "Post-Renovation Upside") {
                    InputRow(
                        label = "ADR Premium ($ increase)",
                        value = inputs.pipPostRenovationAdrPremium.toDollarInput(),
                        onValueChange = { vm.setPipPostRenovationAdrPremium(it.toDoubleOrDefault()) },
                        prefix = "$",
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(
                        "ADR premium applied from Year 3 onwards after renovation completion.",
                        style = MaterialTheme.typography.bodySmall,
                    )
                }

                Spacer(modifier = Modifier.height(16.dp))

                // PIP impact summary
                ValuationCard(title = "PIP Cash Flow Impact") {
                    LineItemRow(
                        label = "",
                        values = (1..5).map { "Year $it" },
                        isHeader = true,
                    )
                    LineItemRow(
                        label = "PIP Spend",
                        values = result.yearProjections.map {
                            if (it.pipExpenditure > 0) "(${Fmt.compactCurrency(it.pipExpenditure)})" else "—"
                        },
                    )
                    LineItemRow(
                        label = "NOI",
                        values = result.yearProjections.map { Fmt.compactCurrency(it.netOperatingIncome) },
                    )
                    LineItemRow(
                        label = "Cash Flow",
                        values = result.yearProjections.map { Fmt.compactCurrency(it.cashFlowAfterPip) },
                        isTotal = true,
                    )
                }
            }

            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
