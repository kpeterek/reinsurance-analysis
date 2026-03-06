package com.hotelvaluation.model

/**
 * Complete hotel valuation input model.
 * All monetary values in dollars, rates as decimals (0.05 = 5%).
 */
data class HotelInputs(
    // Property basics
    val propertyName: String = "Subject Hotel",
    val numberOfRooms: Int = 200,
    val occupancyRate: Double = 0.70,
    val adr: Double = 185.0, // Average Daily Rate

    // Revenue breakdown (as % of gross room revenue)
    val foodBeveragePctOfRevenue: Double = 0.25,
    val otherIncomePctOfRevenue: Double = 0.05,

    // Departmental expenses (as % of respective departmental revenue)
    val roomsExpensePct: Double = 0.25,
    val fbExpensePct: Double = 0.72,
    val otherExpensePct: Double = 0.50,

    // Undistributed operating expenses (as % of total revenue)
    val adminGeneralPct: Double = 0.08,
    val marketingPct: Double = 0.05,
    val propOperationsPct: Double = 0.04,
    val utilityPct: Double = 0.03,

    // Fixed charges (as % of total revenue)
    val insurancePct: Double = 0.015,
    val propertyTaxPct: Double = 0.03,
    val managementFeePct: Double = 0.03,
    val franchiseFeePct: Double = 0.05,

    // Reserve for replacement (as % of total revenue)
    val reserveForReplacementPct: Double = 0.04,

    // Growth rates
    val revenueGrowthRate: Double = 0.03,
    val expenseGrowthRate: Double = 0.025,
    val occupancyGrowthRate: Double = 0.01,  // annual occupancy point increase
    val adrGrowthRate: Double = 0.03,

    // DCF parameters
    val discountRate: Double = 0.10,
    val terminalCapRate: Double = 0.085,

    // PIP (Property Improvement Plan)
    val pipEnabled: Boolean = false,
    val pipTotalCost: Double = 0.0,
    val pipYear1Pct: Double = 0.60,  // % of PIP spent in year 1
    val pipYear2Pct: Double = 0.40,  // % of PIP spent in year 2
    val pipRevenueDisruptionYear1: Double = 0.0, // revenue reduction during PIP
    val pipRevenueDisruptionYear2: Double = 0.0,
    val pipPostRenovationAdrPremium: Double = 0.0, // ADR premium after renovation

    // Per-unit overrides (PAR / POR mode)
    val inputMode: InputMode = InputMode.PERCENTAGE,

    // PAR (Per Available Room) fixed dollar amounts (annual)
    val adminGeneralPar: Double = 0.0,
    val marketingPar: Double = 0.0,
    val propOperationsPar: Double = 0.0,
    val utilityPar: Double = 0.0,
    val insurancePar: Double = 0.0,
    val propertyTaxPar: Double = 0.0,
)

enum class InputMode {
    PERCENTAGE,   // % of gross revenue
    POR,          // Per Occupied Room
    PAR           // Per Available Room
}
