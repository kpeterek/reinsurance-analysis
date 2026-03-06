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
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.Fmt

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProFormaScreen(
    result: ValuationResult,
    onBack: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Burgundy900),
    ) {
        TopAppBar(
            title = { Text("5-Year Pro Forma") },
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
            val years = result.yearProjections
            val yearLabels = years.map { "Year ${it.year}" }

            // Revenue
            ValuationCard(title = "Revenue") {
                Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                    Column(modifier = Modifier.widthIn(min = 600.dp)) {
                        LineItemRow("", yearLabels, isHeader = true)
                        LineItemRow("Room Revenue", years.map { Fmt.compactCurrency(it.roomRevenue) })
                        LineItemRow("F&B Revenue", years.map { Fmt.compactCurrency(it.fbRevenue) })
                        LineItemRow("Other Income", years.map { Fmt.compactCurrency(it.otherRevenue) })
                        LineItemRow("Total Revenue", years.map { Fmt.compactCurrency(it.totalRevenue) }, isTotal = true)
                    }
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Departmental Expenses
            ValuationCard(title = "Departmental Expenses") {
                Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                    Column(modifier = Modifier.widthIn(min = 600.dp)) {
                        LineItemRow("", yearLabels, isHeader = true)
                        LineItemRow("Rooms", years.map { Fmt.compactCurrency(it.roomsExpense) })
                        LineItemRow("F&B", years.map { Fmt.compactCurrency(it.fbExpense) })
                        LineItemRow("Other", years.map { Fmt.compactCurrency(it.otherExpense) })
                        LineItemRow("Total Dept Expense", years.map { Fmt.compactCurrency(it.totalDeptExpense) }, isTotal = true)
                        LineItemRow("Dept Profit", years.map { Fmt.compactCurrency(it.departmentalProfit) }, isTotal = true)
                    }
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Undistributed Expenses
            ValuationCard(title = "Undistributed Operating Expenses") {
                Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                    Column(modifier = Modifier.widthIn(min = 600.dp)) {
                        LineItemRow("", yearLabels, isHeader = true)
                        LineItemRow("Admin & General", years.map { Fmt.compactCurrency(it.adminGeneral) })
                        LineItemRow("Marketing", years.map { Fmt.compactCurrency(it.marketing) })
                        LineItemRow("Prop Operations", years.map { Fmt.compactCurrency(it.propOperations) })
                        LineItemRow("Utilities", years.map { Fmt.compactCurrency(it.utility) })
                        LineItemRow("Total Undistributed", years.map { Fmt.compactCurrency(it.totalUndistributed) }, isTotal = true)
                        LineItemRow("Gross Operating Profit", years.map { Fmt.compactCurrency(it.grossOperatingProfit) }, isTotal = true)
                    }
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Fixed Charges
            ValuationCard(title = "Fixed Charges & NOI") {
                Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                    Column(modifier = Modifier.widthIn(min = 600.dp)) {
                        LineItemRow("", yearLabels, isHeader = true)
                        LineItemRow("Insurance", years.map { Fmt.compactCurrency(it.insurance) })
                        LineItemRow("Property Tax", years.map { Fmt.compactCurrency(it.propertyTax) })
                        LineItemRow("Management Fee", years.map { Fmt.compactCurrency(it.managementFee) })
                        LineItemRow("Franchise Fee", years.map { Fmt.compactCurrency(it.franchiseFee) })
                        LineItemRow("Total Fixed", years.map { Fmt.compactCurrency(it.totalFixedCharges) }, isTotal = true)
                        LineItemRow("EBITDA", years.map { Fmt.compactCurrency(it.ebitda) }, isTotal = true)
                        LineItemRow("FF&E Reserve", years.map { Fmt.compactCurrency(it.reserveForReplacement) })
                        LineItemRow("Net Operating Income", years.map { Fmt.compactCurrency(it.netOperatingIncome) }, isTotal = true)
                    }
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // PIP & Cash Flow
            val hasPip = years.any { it.pipExpenditure > 0 }
            if (hasPip) {
                ValuationCard(title = "PIP & Net Cash Flow") {
                    Column(modifier = Modifier.horizontalScroll(rememberScrollState())) {
                        Column(modifier = Modifier.widthIn(min = 600.dp)) {
                            LineItemRow("", yearLabels, isHeader = true)
                            LineItemRow("PIP Expenditure", years.map {
                                if (it.pipExpenditure > 0) "(${Fmt.compactCurrency(it.pipExpenditure)})" else "—"
                            })
                            LineItemRow("Cash Flow After PIP", years.map { Fmt.compactCurrency(it.cashFlowAfterPip) }, isTotal = true)
                        }
                    }
                }
                Spacer(modifier = Modifier.height(12.dp))
            }

            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
