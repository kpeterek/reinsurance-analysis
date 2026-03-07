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
import com.hotelvaluation.model.InputMode
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.HotelValuationViewModel
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun InputsScreen(
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
            title = { Text("Property & Revenue") },
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

        // Live value banner
        LiveValueBanner(result)

        Column(
            modifier = Modifier
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
        ) {
            // Property basics
            ValuationCard(title = "Property Details") {
                ValuationTextField(
                    label = "Property Name",
                    value = inputs.propertyName,
                    onValueChange = { vm.setPropertyName(it) },
                )
                Spacer(modifier = Modifier.height(8.dp))
                InputRow(
                    label = "Number of Rooms",
                    value = inputs.numberOfRooms.toString(),
                    onValueChange = { vm.setNumberOfRooms(it.toIntOrNull() ?: 200) },
                )
                InputRow(
                    label = "Occupancy Rate",
                    value = inputs.occupancyRate.toPctInput(),
                    onValueChange = { vm.setOccupancyRate(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "Average Daily Rate",
                    value = inputs.adr.toDollarInput(),
                    onValueChange = { vm.setAdr(it.toDoubleOrDefault(185.0)) },
                    prefix = "$",
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Revenue mix
            ValuationCard(title = "Revenue Mix (% of Room Revenue)") {
                InputRow(
                    label = "Food & Beverage",
                    value = inputs.foodBeveragePctOfRevenue.toPctInput(),
                    onValueChange = { vm.setFbPct(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "Other Income",
                    value = inputs.otherIncomePctOfRevenue.toPctInput(),
                    onValueChange = { vm.setOtherIncomePct(it.fromPctInput()) },
                    isPercentage = true,
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Departmental expenses
            ValuationCard(title = "Departmental Expenses (% of Dept Revenue)") {
                InputRow(
                    label = "Rooms Expense",
                    value = inputs.roomsExpensePct.toPctInput(),
                    onValueChange = { vm.setRoomsExpensePct(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "F&B Expense",
                    value = inputs.fbExpensePct.toPctInput(),
                    onValueChange = { vm.setFbExpensePct(it.fromPctInput()) },
                    isPercentage = true,
                )
                InputRow(
                    label = "Other Dept Expense",
                    value = inputs.otherExpensePct.toPctInput(),
                    onValueChange = { vm.setOtherExpensePct(it.fromPctInput()) },
                    isPercentage = true,
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Input mode selector
            ValuationCard(title = "Undistributed Expenses") {
                val modeLabel = when (inputs.inputMode) {
                    InputMode.PERCENTAGE -> "% Revenue"
                    InputMode.PAR -> "PAR"
                    InputMode.POR -> "POR"
                }
                InputModeSelector(
                    selectedMode = modeLabel,
                    onModeSelected = { mode ->
                        vm.setInputMode(
                            when (mode) {
                                "PAR" -> InputMode.PAR
                                "POR" -> InputMode.POR
                                else -> InputMode.PERCENTAGE
                            }
                        )
                    }
                )
                Spacer(modifier = Modifier.height(12.dp))

                if (inputs.inputMode == InputMode.PERCENTAGE) {
                    InputRow("Admin & General", inputs.adminGeneralPct.toPctInput(),
                        { vm.setAdminGeneralPct(it.fromPctInput()) }, isPercentage = true)
                    InputRow("Sales & Marketing", inputs.marketingPct.toPctInput(),
                        { vm.setMarketingPct(it.fromPctInput()) }, isPercentage = true)
                    InputRow("Property Operations", inputs.propOperationsPct.toPctInput(),
                        { vm.setPropOperationsPct(it.fromPctInput()) }, isPercentage = true)
                    InputRow("Utilities", inputs.utilityPct.toPctInput(),
                        { vm.setUtilityPct(it.fromPctInput()) }, isPercentage = true)
                } else {
                    val suffix = if (inputs.inputMode == InputMode.PAR) "/room/yr" else "/occ night"
                    InputRow("Admin & General", inputs.adminGeneralPar.toDollarInput(),
                        { vm.setAdminGeneralPar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                    InputRow("Sales & Marketing", inputs.marketingPar.toDollarInput(),
                        { vm.setMarketingPar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                    InputRow("Property Operations", inputs.propOperationsPar.toDollarInput(),
                        { vm.setPropOperationsPar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                    InputRow("Utilities", inputs.utilityPar.toDollarInput(),
                        { vm.setUtilityPar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Fixed charges
            ValuationCard(title = "Fixed Charges") {
                if (inputs.inputMode == InputMode.PERCENTAGE) {
                    InputRow("Insurance", inputs.insurancePct.toPctInput(),
                        { vm.setInsurancePct(it.fromPctInput()) }, isPercentage = true)
                    InputRow("Property Tax", inputs.propertyTaxPct.toPctInput(),
                        { vm.setPropertyTaxPct(it.fromPctInput()) }, isPercentage = true)
                } else {
                    val suffix = if (inputs.inputMode == InputMode.PAR) "/room/yr" else "/occ night"
                    InputRow("Insurance", inputs.insurancePar.toDollarInput(),
                        { vm.setInsurancePar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                    InputRow("Property Tax", inputs.propertyTaxPar.toDollarInput(),
                        { vm.setPropertyTaxPar(it.toDoubleOrDefault()) }, prefix = "$", suffix = suffix)
                }
                InputRow("Management Fee", inputs.managementFeePct.toPctInput(),
                    { vm.setManagementFeePct(it.fromPctInput()) }, isPercentage = true)
                InputRow("Franchise Fee", inputs.franchiseFeePct.toPctInput(),
                    { vm.setFranchiseFeePct(it.fromPctInput()) }, isPercentage = true)
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Reserve
            ValuationCard(title = "Reserve for Replacement") {
                InputRow("FF&E Reserve", inputs.reserveForReplacementPct.toPctInput(),
                    { vm.setReserveForReplacementPct(it.fromPctInput()) }, isPercentage = true)
            }

            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}

@Composable
fun LiveValueBanner(result: ValuationResult) {
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .background(
                Brush.horizontalGradient(
                    listOf(Burgundy700, RichRed.copy(alpha = 0.3f), Burgundy700)
                )
            )
            .padding(vertical = 12.dp, horizontal = 16.dp),
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
        ) {
            Column {
                Text("LIVE VALUATION", style = MaterialTheme.typography.labelMedium)
                Text(
                    Fmt.compactCurrency(result.totalPropertyValue),
                    style = MaterialTheme.typography.headlineSmall.copy(color = ChampagneGold),
                )
            }
            Column(horizontalAlignment = androidx.compose.ui.Alignment.End) {
                Text("PER ROOM", style = MaterialTheme.typography.labelMedium)
                Text(
                    Fmt.compactCurrency(result.valuePerRoom),
                    style = MaterialTheme.typography.headlineSmall.copy(color = ChampagneGold),
                )
            }
        }
    }
}
