package com.hotelvaluation.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.Fmt

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DCFScreen(
    inputs: HotelInputs,
    result: ValuationResult,
    onBack: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Burgundy900),
    ) {
        TopAppBar(
            title = { Text("DCF Analysis") },
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

        Column(
            modifier = Modifier
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
        ) {
            // Valuation summary
            ValuationCard(title = "Valuation Summary") {
                ValuationFigure(
                    label = "Total Property Value",
                    value = Fmt.compactCurrency(result.totalPropertyValue),
                    modifier = Modifier.fillMaxWidth(),
                    subtext = "${Fmt.compactCurrency(result.valuePerRoom)} per room",
                )

                ArtDecoDivider()

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly,
                ) {
                    ValuationFigure(
                        label = "Implied Cap",
                        value = Fmt.pct(result.impliedCapRate),
                        modifier = Modifier.weight(1f),
                        valueColor = RoseGold,
                    )
                    ValuationFigure(
                        label = "NOI Multiple",
                        value = Fmt.multiplier(result.impliedMultiple),
                        modifier = Modifier.weight(1f),
                        valueColor = RoseGold,
                    )
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // DCF breakdown
            ValuationCard(title = "Present Value of Cash Flows") {
                val years = result.yearProjections
                Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                    Column(modifier = Modifier.widthIn(min = 600.dp)) {
                        LineItemRow(
                            label = "",
                            values = years.map { "Year ${it.year}" },
                            isHeader = true,
                        )
                        LineItemRow(
                            label = "Cash Flow",
                            values = years.map { Fmt.compactCurrency(it.cashFlowAfterPip) },
                        )
                        LineItemRow(
                            label = "Discount Factor",
                            values = years.map { Fmt.decimal(it.discountFactor) },
                        )
                        LineItemRow(
                            label = "Present Value",
                            values = years.map { Fmt.compactCurrency(it.presentValue) },
                            isTotal = true,
                        )
                    }
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Value composition
            ValuationCard(title = "Value Composition") {
                SummaryRow("PV of Operating Cash Flows", Fmt.currency(result.totalPvCashFlows))
                SummaryRow("Terminal Value (Year 5)", Fmt.currency(result.terminalValue))
                SummaryRow("PV of Terminal Value", Fmt.currency(result.pvTerminalValue))

                Spacer(modifier = Modifier.height(8.dp))
                HorizontalDivider(color = Burgundy500)
                Spacer(modifier = Modifier.height(8.dp))

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                ) {
                    Text(
                        "Total Property Value",
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.Bold,
                            color = RoseGold,
                        ),
                    )
                    Text(
                        Fmt.currency(result.totalPropertyValue),
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.Bold,
                            color = ChampagneGold,
                        ),
                    )
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Assumptions
            ValuationCard(title = "Key Assumptions") {
                SummaryRow("Discount Rate", Fmt.pct(inputs.discountRate))
                SummaryRow("Terminal Cap Rate", Fmt.pct(inputs.terminalCapRate))
                SummaryRow("Revenue Growth", Fmt.pct(inputs.adrGrowthRate))
                SummaryRow("Expense Growth", Fmt.pct(inputs.expenseGrowthRate))
                SummaryRow("Holding Period", "5 Years")
                if (inputs.pipEnabled) {
                    SummaryRow("PIP Investment", Fmt.currency(inputs.pipTotalCost))
                }
            }

            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}

@Composable
private fun SummaryRow(label: String, value: String) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(label, style = MaterialTheme.typography.bodyMedium)
        Text(
            value,
            style = MaterialTheme.typography.bodyMedium.copy(
                fontWeight = FontWeight.SemiBold,
                color = ChampagneGold,
            ),
        )
    }
}
