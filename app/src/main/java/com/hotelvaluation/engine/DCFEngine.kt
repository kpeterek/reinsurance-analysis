package com.hotelvaluation.engine

import com.hotelvaluation.model.*
import kotlin.math.min
import kotlin.math.pow

/**
 * Discounted Cash Flow valuation engine for hotel properties.
 * Produces a 5-year pro forma with terminal value calculation.
 */
object DCFEngine {

    fun calculate(inputs: HotelInputs): ValuationResult {
        val projections = mutableListOf<YearProjection>()
        var totalPvCashFlows = 0.0

        for (year in 1..5) {
            val projection = projectYear(inputs, year)
            projections.add(projection)
            totalPvCashFlows += projection.presentValue
        }

        // Terminal value based on Year 5 NOI
        val year5Noi = projections.last().netOperatingIncome
        val terminalValue = year5Noi * (1 + inputs.revenueGrowthRate) / inputs.terminalCapRate
        val discountFactor = 1.0 / (1 + inputs.discountRate).pow(5)
        val pvTerminalValue = terminalValue * discountFactor

        val totalPropertyValue = totalPvCashFlows + pvTerminalValue
        val valuePerRoom = totalPropertyValue / inputs.numberOfRooms
        val year1Noi = projections.first().netOperatingIncome
        val impliedCapRate = if (totalPropertyValue > 0) year1Noi / totalPropertyValue else 0.0
        val impliedMultiple = if (year1Noi > 0) totalPropertyValue / year1Noi else 0.0

        return ValuationResult(
            yearProjections = projections,
            totalPvCashFlows = totalPvCashFlows,
            terminalValue = terminalValue,
            pvTerminalValue = pvTerminalValue,
            totalPropertyValue = totalPropertyValue,
            valuePerRoom = valuePerRoom,
            impliedCapRate = impliedCapRate,
            impliedMultiple = impliedMultiple,
        )
    }

    private fun projectYear(inputs: HotelInputs, year: Int): YearProjection {
        val rooms = inputs.numberOfRooms
        val daysInYear = 365.0

        // Occupancy grows by fixed points per year, capped at 95%
        val occupancy = min(
            inputs.occupancyRate + (inputs.occupancyGrowthRate * (year - 1)),
            0.95
        )

        // ADR grows annually, plus PIP premium after year 2
        var adr = inputs.adr * (1 + inputs.adrGrowthRate).pow(year - 1)
        if (inputs.pipEnabled && year >= 3) {
            adr += inputs.pipPostRenovationAdrPremium
        }

        val revPar = occupancy * adr
        val totalRoomNights = rooms * daysInYear
        val occupiedRoomNights = totalRoomNights * occupancy

        // Revenue
        var roomRevenue = occupiedRoomNights * adr

        // PIP revenue disruption
        if (inputs.pipEnabled) {
            when (year) {
                1 -> roomRevenue *= (1 - inputs.pipRevenueDisruptionYear1)
                2 -> roomRevenue *= (1 - inputs.pipRevenueDisruptionYear2)
            }
        }

        val fbRevenue = roomRevenue * inputs.foodBeveragePctOfRevenue
        val otherRevenue = roomRevenue * inputs.otherIncomePctOfRevenue
        val totalRevenue = roomRevenue + fbRevenue + otherRevenue

        // Departmental expenses
        val roomsExpense = roomRevenue * inputs.roomsExpensePct
        val fbExpense = fbRevenue * inputs.fbExpensePct
        val otherExpense = otherRevenue * inputs.otherExpensePct
        val totalDeptExpense = roomsExpense + fbExpense + otherExpense
        val departmentalProfit = totalRevenue - totalDeptExpense

        // Undistributed expenses - support multiple input modes
        val expGrowth = (1 + inputs.expenseGrowthRate).pow(year - 1)

        val adminGeneral = calculateExpense(
            inputs.inputMode, inputs.adminGeneralPct, inputs.adminGeneralPar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val marketing = calculateExpense(
            inputs.inputMode, inputs.marketingPct, inputs.marketingPar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val propOperations = calculateExpense(
            inputs.inputMode, inputs.propOperationsPct, inputs.propOperationsPar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val utility = calculateExpense(
            inputs.inputMode, inputs.utilityPct, inputs.utilityPar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val totalUndistributed = adminGeneral + marketing + propOperations + utility

        val grossOperatingProfit = departmentalProfit - totalUndistributed

        // Fixed charges
        val insurance = calculateExpense(
            inputs.inputMode, inputs.insurancePct, inputs.insurancePar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val propertyTax = calculateExpense(
            inputs.inputMode, inputs.propertyTaxPct, inputs.propertyTaxPar,
            totalRevenue, rooms, occupiedRoomNights, expGrowth
        )
        val managementFee = totalRevenue * inputs.managementFeePct
        val franchiseFee = roomRevenue * inputs.franchiseFeePct
        val totalFixedCharges = insurance + propertyTax + managementFee + franchiseFee

        val ebitda = grossOperatingProfit - totalFixedCharges

        // Reserve for replacement
        val reserveForReplacement = totalRevenue * inputs.reserveForReplacementPct

        val noi = ebitda - reserveForReplacement

        // PIP expenditure
        val pipExpenditure = if (inputs.pipEnabled) {
            when (year) {
                1 -> inputs.pipTotalCost * inputs.pipYear1Pct
                2 -> inputs.pipTotalCost * inputs.pipYear2Pct
                else -> 0.0
            }
        } else 0.0

        val cashFlowAfterPip = noi - pipExpenditure

        val discountFactor = 1.0 / (1 + inputs.discountRate).pow(year)
        val presentValue = cashFlowAfterPip * discountFactor

        return YearProjection(
            year = year,
            occupancy = occupancy,
            adr = adr,
            revPar = revPar,
            roomRevenue = roomRevenue,
            fbRevenue = fbRevenue,
            otherRevenue = otherRevenue,
            totalRevenue = totalRevenue,
            roomsExpense = roomsExpense,
            fbExpense = fbExpense,
            otherExpense = otherExpense,
            totalDeptExpense = totalDeptExpense,
            departmentalProfit = departmentalProfit,
            adminGeneral = adminGeneral,
            marketing = marketing,
            propOperations = propOperations,
            utility = utility,
            totalUndistributed = totalUndistributed,
            grossOperatingProfit = grossOperatingProfit,
            insurance = insurance,
            propertyTax = propertyTax,
            managementFee = managementFee,
            franchiseFee = franchiseFee,
            totalFixedCharges = totalFixedCharges,
            ebitda = ebitda,
            reserveForReplacement = reserveForReplacement,
            netOperatingIncome = noi,
            pipExpenditure = pipExpenditure,
            cashFlowAfterPip = cashFlowAfterPip,
            discountFactor = discountFactor,
            presentValue = presentValue,
        )
    }

    private fun calculateExpense(
        mode: InputMode,
        pctOfRevenue: Double,
        parAmount: Double,
        totalRevenue: Double,
        rooms: Int,
        occupiedRoomNights: Double,
        expenseGrowth: Double,
    ): Double {
        return when (mode) {
            InputMode.PERCENTAGE -> totalRevenue * pctOfRevenue
            InputMode.PAR -> parAmount * rooms * expenseGrowth
            InputMode.POR -> parAmount * occupiedRoomNights * expenseGrowth
        }
    }
}
