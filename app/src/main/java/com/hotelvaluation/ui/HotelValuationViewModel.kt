package com.hotelvaluation.ui

import androidx.lifecycle.ViewModel
import com.hotelvaluation.engine.DCFEngine
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.InputMode
import com.hotelvaluation.model.ValuationResult
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class HotelValuationViewModel : ViewModel() {

    private val _inputs = MutableStateFlow(HotelInputs())
    val inputs: StateFlow<HotelInputs> = _inputs.asStateFlow()

    private val _result = MutableStateFlow(DCFEngine.calculate(HotelInputs()))
    val result: StateFlow<ValuationResult> = _result.asStateFlow()

    fun updateInputs(transform: HotelInputs.() -> HotelInputs) {
        val newInputs = _inputs.value.transform()
        _inputs.value = newInputs
        _result.value = DCFEngine.calculate(newInputs)
    }

    fun setPropertyName(name: String) = updateInputs { copy(propertyName = name) }
    fun setNumberOfRooms(rooms: Int) = updateInputs { copy(numberOfRooms = rooms.coerceAtLeast(1)) }
    fun setOccupancyRate(rate: Double) = updateInputs { copy(occupancyRate = rate.coerceIn(0.0, 1.0)) }
    fun setAdr(adr: Double) = updateInputs { copy(adr = adr.coerceAtLeast(0.0)) }

    fun setFbPct(pct: Double) = updateInputs { copy(foodBeveragePctOfRevenue = pct) }
    fun setOtherIncomePct(pct: Double) = updateInputs { copy(otherIncomePctOfRevenue = pct) }

    fun setRoomsExpensePct(pct: Double) = updateInputs { copy(roomsExpensePct = pct) }
    fun setFbExpensePct(pct: Double) = updateInputs { copy(fbExpensePct = pct) }
    fun setOtherExpensePct(pct: Double) = updateInputs { copy(otherExpensePct = pct) }

    fun setAdminGeneralPct(pct: Double) = updateInputs { copy(adminGeneralPct = pct) }
    fun setMarketingPct(pct: Double) = updateInputs { copy(marketingPct = pct) }
    fun setPropOperationsPct(pct: Double) = updateInputs { copy(propOperationsPct = pct) }
    fun setUtilityPct(pct: Double) = updateInputs { copy(utilityPct = pct) }

    fun setInsurancePct(pct: Double) = updateInputs { copy(insurancePct = pct) }
    fun setPropertyTaxPct(pct: Double) = updateInputs { copy(propertyTaxPct = pct) }
    fun setManagementFeePct(pct: Double) = updateInputs { copy(managementFeePct = pct) }
    fun setFranchiseFeePct(pct: Double) = updateInputs { copy(franchiseFeePct = pct) }

    fun setReserveForReplacementPct(pct: Double) = updateInputs { copy(reserveForReplacementPct = pct) }

    fun setRevenueGrowthRate(rate: Double) = updateInputs { copy(revenueGrowthRate = rate) }
    fun setExpenseGrowthRate(rate: Double) = updateInputs { copy(expenseGrowthRate = rate) }
    fun setOccupancyGrowthRate(rate: Double) = updateInputs { copy(occupancyGrowthRate = rate) }
    fun setAdrGrowthRate(rate: Double) = updateInputs { copy(adrGrowthRate = rate) }

    fun setDiscountRate(rate: Double) = updateInputs { copy(discountRate = rate.coerceIn(0.01, 0.50)) }
    fun setTerminalCapRate(rate: Double) = updateInputs { copy(terminalCapRate = rate.coerceIn(0.01, 0.50)) }

    fun setInputMode(mode: InputMode) = updateInputs { copy(inputMode = mode) }

    // PAR setters
    fun setAdminGeneralPar(amount: Double) = updateInputs { copy(adminGeneralPar = amount) }
    fun setMarketingPar(amount: Double) = updateInputs { copy(marketingPar = amount) }
    fun setPropOperationsPar(amount: Double) = updateInputs { copy(propOperationsPar = amount) }
    fun setUtilityPar(amount: Double) = updateInputs { copy(utilityPar = amount) }
    fun setInsurancePar(amount: Double) = updateInputs { copy(insurancePar = amount) }
    fun setPropertyTaxPar(amount: Double) = updateInputs { copy(propertyTaxPar = amount) }

    // PIP setters
    fun setPipEnabled(enabled: Boolean) = updateInputs { copy(pipEnabled = enabled) }
    fun setPipTotalCost(cost: Double) = updateInputs { copy(pipTotalCost = cost) }
    fun setPipYear1Pct(pct: Double) = updateInputs { copy(pipYear1Pct = pct, pipYear2Pct = 1.0 - pct) }
    fun setPipRevenueDisruptionYear1(pct: Double) = updateInputs { copy(pipRevenueDisruptionYear1 = pct) }
    fun setPipRevenueDisruptionYear2(pct: Double) = updateInputs { copy(pipRevenueDisruptionYear2 = pct) }
    fun setPipPostRenovationAdrPremium(premium: Double) = updateInputs { copy(pipPostRenovationAdrPremium = premium) }
}
