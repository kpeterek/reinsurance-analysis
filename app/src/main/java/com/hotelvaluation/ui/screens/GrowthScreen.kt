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
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.unit.dp
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.HotelValuationViewModel
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun GrowthScreen(
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
            title = { Text("Growth Assumptions") },
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
            ValuationCard(title = "Revenue Growth") {
                InputRow(
                    label = "ADR Growth Rate",
                    value = inputs.adrGrowthRate.toPctInput(),
                    onValueChange = { vm.setAdrGrowthRate(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "Occupancy Growth (pts/yr)",
                    value = inputs.occupancyGrowthRate.toPctInput(),
                    onValueChange = { vm.setOccupancyGrowthRate(it.fromPctInput()) },
                    isPercentage = true,
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            ValuationCard(title = "Expense Growth") {
                InputRow(
                    label = "Expense Growth Rate",
                    value = inputs.expenseGrowthRate.toPctInput(),
                    onValueChange = { vm.setExpenseGrowthRate(it.fromPctInput()) },
                    isPercentage = true,
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            ValuationCard(title = "DCF Parameters") {
                InputRow(
                    label = "Discount Rate",
                    value = inputs.discountRate.toPctInput(),
                    onValueChange = { vm.setDiscountRate(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "Terminal Cap Rate",
                    value = inputs.terminalCapRate.toPctInput(),
                    onValueChange = { vm.setTerminalCapRate(it.fromPctInput()) },
                    isPercentage = true,
                )
            }

            Spacer(modifier = Modifier.height(24.dp))

            // Growth impact preview
            ValuationCard(title = "5-Year Growth Preview") {
                LineItemRow(
                    label = "",
                    values = (1..5).map { "Year $it" },
                    isHeader = true,
                )
                LineItemRow(
                    label = "Occupancy",
                    values = result.yearProjections.map { Fmt.pct(it.occupancy) },
                )
                LineItemRow(
                    label = "ADR",
                    values = result.yearProjections.map { Fmt.currency(it.adr) },
                )
                LineItemRow(
                    label = "RevPAR",
                    values = result.yearProjections.map { Fmt.currency(it.revPar) },
                )
                LineItemRow(
                    label = "NOI",
                    values = result.yearProjections.map { Fmt.compactCurrency(it.netOperatingIncome) },
                    isTotal = true,
                )
            }

            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
