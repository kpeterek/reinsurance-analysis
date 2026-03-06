package com.hotelvaluation.export

import android.content.Context
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.model.YearProjection
import com.hotelvaluation.util.Fmt
import com.itextpdf.kernel.colors.ColorConstants
import com.itextpdf.kernel.colors.DeviceRgb
import com.itextpdf.kernel.geom.PageSize
import com.itextpdf.kernel.pdf.PdfDocument
import com.itextpdf.kernel.pdf.PdfWriter
import com.itextpdf.kernel.pdf.canvas.draw.SolidLine
import com.itextpdf.layout.Document
import com.itextpdf.layout.borders.Border
import com.itextpdf.layout.borders.SolidBorder
import com.itextpdf.layout.element.*
import com.itextpdf.layout.properties.HorizontalAlignment
import com.itextpdf.layout.properties.TextAlignment
import com.itextpdf.layout.properties.UnitValue
import com.itextpdf.layout.properties.VerticalAlignment
import java.io.File
import java.time.LocalDate
import java.time.format.DateTimeFormatter

/**
 * Generates a beautiful art deco themed PDF valuation report.
 */
object PdfReportGenerator {

    // Art Deco color palette
    private val BURGUNDY_DARK = DeviceRgb(26, 10, 10)
    private val BURGUNDY = DeviceRgb(75, 26, 32)
    private val RICH_RED = DeviceRgb(162, 59, 72)
    private val ROSE_GOLD = DeviceRgb(212, 165, 116)
    private val CHAMPAGNE = DeviceRgb(232, 213, 181)
    private val IVORY = DeviceRgb(255, 248, 240)
    private val DARK_TABLE = DeviceRgb(45, 17, 20)
    private val TABLE_ALT = DeviceRgb(58, 22, 28)

    fun generate(
        context: Context,
        inputs: HotelInputs,
        result: ValuationResult,
    ): File {
        val reportDir = File(context.cacheDir, "reports")
        reportDir.mkdirs()
        val file = File(reportDir, "Hotel_Valuation_${System.currentTimeMillis()}.pdf")

        val writer = PdfWriter(file)
        val pdf = PdfDocument(writer)
        val document = Document(pdf, PageSize.LETTER)
        document.setMargins(50f, 50f, 50f, 50f)

        // ── Cover Page ──
        addCoverPage(document, inputs, result)
        document.add(AreaBreak())

        // ── Executive Summary ──
        addExecutiveSummary(document, inputs, result)
        document.add(AreaBreak())

        // ── 5-Year Pro Forma ──
        addProForma(document, inputs, result)
        document.add(AreaBreak())

        // ── DCF Analysis ──
        addDcfAnalysis(document, inputs, result)

        // ── Assumptions & Disclaimer ──
        document.add(AreaBreak())
        addAssumptions(document, inputs)

        document.close()
        return file
    }

    private fun addCoverPage(document: Document, inputs: HotelInputs, result: ValuationResult) {
        document.add(Paragraph("\n\n\n\n"))

        // Art deco top border
        addDecoDivider(document)

        document.add(Paragraph("\n"))

        document.add(
            Paragraph("HOTEL VALUATION")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(14f)
                .setFontColor(ROSE_GOLD)
                .setCharacterSpacing(6f)
        )

        document.add(
            Paragraph("ANALYSIS & REPORT")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(11f)
                .setFontColor(ROSE_GOLD)
                .setCharacterSpacing(4f)
        )

        document.add(Paragraph("\n"))

        document.add(
            Paragraph(inputs.propertyName)
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(32f)
                .setFontColor(BURGUNDY_DARK)
                .setBold()
        )

        document.add(Paragraph("\n"))
        addDecoDivider(document)
        document.add(Paragraph("\n\n"))

        // Key figures on cover
        val coverTable = Table(UnitValue.createPercentArray(3))
            .useAllAvailableWidth()
            .setBorder(Border.NO_BORDER)

        coverTable.addCell(coverMetricCell("TOTAL VALUE", Fmt.compactCurrency(result.totalPropertyValue)))
        coverTable.addCell(coverMetricCell("VALUE PER ROOM", Fmt.compactCurrency(result.valuePerRoom)))
        coverTable.addCell(coverMetricCell("IMPLIED CAP RATE", Fmt.pct(result.impliedCapRate)))

        document.add(coverTable)

        document.add(Paragraph("\n\n\n"))
        addDecoDivider(document)

        document.add(Paragraph("\n\n"))
        document.add(
            Paragraph("Prepared: ${LocalDate.now().format(DateTimeFormatter.ofPattern("d MMMM yyyy"))}")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(10f)
                .setFontColor(RICH_RED)
        )
        document.add(
            Paragraph("${inputs.numberOfRooms} Rooms | ${Fmt.pct(inputs.occupancyRate)} Occupancy | ${Fmt.currencyDetail(inputs.adr)} ADR")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(10f)
                .setFontColor(BURGUNDY)
        )

        document.add(Paragraph("\n\n\n"))
        document.add(
            Paragraph("CONFIDENTIAL")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(9f)
                .setFontColor(RICH_RED)
                .setCharacterSpacing(3f)
        )
    }

    private fun coverMetricCell(label: String, value: String): Cell {
        return Cell()
            .setBorder(Border.NO_BORDER)
            .setTextAlignment(TextAlignment.CENTER)
            .setPadding(10f)
            .add(
                Paragraph(label)
                    .setFontSize(8f)
                    .setFontColor(RICH_RED)
                    .setCharacterSpacing(2f)
                    .setTextAlignment(TextAlignment.CENTER)
            )
            .add(
                Paragraph(value)
                    .setFontSize(22f)
                    .setFontColor(BURGUNDY_DARK)
                    .setBold()
                    .setTextAlignment(TextAlignment.CENTER)
            )
    }

    private fun addExecutiveSummary(document: Document, inputs: HotelInputs, result: ValuationResult) {
        addSectionTitle(document, "EXECUTIVE SUMMARY")

        val year1 = result.yearProjections.first()
        val year5 = result.yearProjections.last()

        val summaryText = """
            This report presents a Discounted Cash Flow (DCF) valuation analysis for ${inputs.propertyName},
            a ${inputs.numberOfRooms}-room hotel property. The analysis projects operating performance over
            a five-year holding period, discounting projected net cash flows at ${Fmt.pct(inputs.discountRate)}
            with a terminal capitalization rate of ${Fmt.pct(inputs.terminalCapRate)}.
        """.trimIndent().replace("\n", " ")

        document.add(
            Paragraph(summaryText)
                .setFontSize(11f)
                .setFontColor(BURGUNDY_DARK)
                .setMarginBottom(15f)
        )

        // Summary metrics table
        val table = Table(UnitValue.createPercentArray(floatArrayOf(2f, 1f, 1f)))
            .useAllAvailableWidth()
            .setMarginBottom(15f)

        addTableHeader(table, "Metric", "Year 1", "Year 5")
        addTableRow(table, "Total Revenue", Fmt.currency(year1.totalRevenue), Fmt.currency(year5.totalRevenue), false)
        addTableRow(table, "Gross Operating Profit", Fmt.currency(year1.grossOperatingProfit), Fmt.currency(year5.grossOperatingProfit), true)
        addTableRow(table, "EBITDA", Fmt.currency(year1.ebitda), Fmt.currency(year5.ebitda), false)
        addTableRow(table, "Net Operating Income", Fmt.currency(year1.netOperatingIncome), Fmt.currency(year5.netOperatingIncome), true)
        addTableRow(table, "RevPAR", Fmt.currencyDetail(year1.revPar), Fmt.currencyDetail(year5.revPar), false)

        document.add(table)

        // Valuation breakdown
        addSubSectionTitle(document, "VALUATION BREAKDOWN")

        val valTable = Table(UnitValue.createPercentArray(floatArrayOf(3f, 2f)))
            .useAllAvailableWidth()
            .setMarginBottom(15f)

        addValRow(valTable, "Present Value of Cash Flows (Years 1-5)", Fmt.currency(result.totalPvCashFlows), false)
        addValRow(valTable, "Terminal Value", Fmt.currency(result.terminalValue), true)
        addValRow(valTable, "Present Value of Terminal Value", Fmt.currency(result.pvTerminalValue), false)
        addValRow(valTable, "TOTAL PROPERTY VALUE", Fmt.currency(result.totalPropertyValue), true)
        addValRow(valTable, "Value Per Room", Fmt.currency(result.valuePerRoom), false)
        addValRow(valTable, "Implied Capitalization Rate", Fmt.pct(result.impliedCapRate), true)
        addValRow(valTable, "Implied NOI Multiple", Fmt.multiplier(result.impliedMultiple), false)

        document.add(valTable)
    }

    private fun addProForma(document: Document, inputs: HotelInputs, result: ValuationResult) {
        addSectionTitle(document, "FIVE-YEAR PRO FORMA")

        val years = result.yearProjections
        val cols = floatArrayOf(2.5f, 1f, 1f, 1f, 1f, 1f)
        val table = Table(UnitValue.createPercentArray(cols))
            .useAllAvailableWidth()
            .setFontSize(9f)

        // Headers
        addTableHeader(table, "", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5")

        // Operating Statistics
        addGroupHeader(table, "OPERATING STATISTICS", 6)
        addProFormaRow(table, "Occupancy", years.map { Fmt.pct(it.occupancy) }, false)
        addProFormaRow(table, "ADR", years.map { Fmt.currencyDetail(it.adr) }, true)
        addProFormaRow(table, "RevPAR", years.map { Fmt.currencyDetail(it.revPar) }, false)

        // Revenue
        addGroupHeader(table, "REVENUE", 6)
        addProFormaRow(table, "Room Revenue", years.map { Fmt.currency(it.roomRevenue) }, false)
        addProFormaRow(table, "Food & Beverage", years.map { Fmt.currency(it.fbRevenue) }, true)
        addProFormaRow(table, "Other Income", years.map { Fmt.currency(it.otherRevenue) }, false)
        addProFormaTotalRow(table, "Total Revenue", years.map { Fmt.currency(it.totalRevenue) })

        // Dept Expenses
        addGroupHeader(table, "DEPARTMENTAL EXPENSES", 6)
        addProFormaRow(table, "Rooms", years.map { Fmt.currency(it.roomsExpense) }, false)
        addProFormaRow(table, "Food & Beverage", years.map { Fmt.currency(it.fbExpense) }, true)
        addProFormaRow(table, "Other", years.map { Fmt.currency(it.otherExpense) }, false)
        addProFormaTotalRow(table, "Total Dept Expenses", years.map { Fmt.currency(it.totalDeptExpense) })
        addProFormaTotalRow(table, "Departmental Profit", years.map { Fmt.currency(it.departmentalProfit) })

        // Undistributed
        addGroupHeader(table, "UNDISTRIBUTED EXPENSES", 6)
        addProFormaRow(table, "Admin & General", years.map { Fmt.currency(it.adminGeneral) }, false)
        addProFormaRow(table, "Sales & Marketing", years.map { Fmt.currency(it.marketing) }, true)
        addProFormaRow(table, "Property Operations", years.map { Fmt.currency(it.propOperations) }, false)
        addProFormaRow(table, "Utilities", years.map { Fmt.currency(it.utility) }, true)
        addProFormaTotalRow(table, "Total Undistributed", years.map { Fmt.currency(it.totalUndistributed) })
        addProFormaTotalRow(table, "Gross Operating Profit", years.map { Fmt.currency(it.grossOperatingProfit) })

        // Fixed Charges
        addGroupHeader(table, "FIXED CHARGES", 6)
        addProFormaRow(table, "Insurance", years.map { Fmt.currency(it.insurance) }, false)
        addProFormaRow(table, "Property Taxes", years.map { Fmt.currency(it.propertyTax) }, true)
        addProFormaRow(table, "Management Fee", years.map { Fmt.currency(it.managementFee) }, false)
        addProFormaRow(table, "Franchise Fee", years.map { Fmt.currency(it.franchiseFee) }, true)
        addProFormaTotalRow(table, "Total Fixed Charges", years.map { Fmt.currency(it.totalFixedCharges) })

        // NOI
        addProFormaTotalRow(table, "EBITDA", years.map { Fmt.currency(it.ebitda) })
        addProFormaRow(table, "FF&E Reserve", years.map { Fmt.currency(it.reserveForReplacement) }, false)
        addProFormaTotalRow(table, "Net Operating Income", years.map { Fmt.currency(it.netOperatingIncome) })

        // PIP
        if (inputs.pipEnabled) {
            addGroupHeader(table, "CAPITAL EXPENDITURE", 6)
            addProFormaRow(table, "PIP Investment", years.map {
                if (it.pipExpenditure > 0) "(${Fmt.currency(it.pipExpenditure)})" else "—"
            }, false)
            addProFormaTotalRow(table, "Cash Flow After PIP", years.map { Fmt.currency(it.cashFlowAfterPip) })
        }

        document.add(table)
    }

    private fun addDcfAnalysis(document: Document, inputs: HotelInputs, result: ValuationResult) {
        addSectionTitle(document, "DCF ANALYSIS")

        val years = result.yearProjections
        val cols = floatArrayOf(2.5f, 1f, 1f, 1f, 1f, 1f)
        val table = Table(UnitValue.createPercentArray(cols))
            .useAllAvailableWidth()
            .setFontSize(9f)

        addTableHeader(table, "", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5")
        addProFormaRow(table, "Net Cash Flow", years.map { Fmt.currency(it.cashFlowAfterPip) }, false)
        addProFormaRow(table, "Discount Factor", years.map { Fmt.decimal(it.discountFactor) }, true)
        addProFormaTotalRow(table, "Present Value", years.map { Fmt.currency(it.presentValue) })

        document.add(table)

        document.add(Paragraph("\n"))

        // Terminal value
        addSubSectionTitle(document, "TERMINAL VALUE CALCULATION")

        document.add(
            Paragraph("Year 5 NOI: ${Fmt.currency(years.last().netOperatingIncome)}")
                .setFontSize(10f).setFontColor(BURGUNDY_DARK)
        )
        document.add(
            Paragraph("Stabilized NOI (Year 6): ${Fmt.currency(years.last().netOperatingIncome * (1 + inputs.revenueGrowthRate))}")
                .setFontSize(10f).setFontColor(BURGUNDY_DARK)
        )
        document.add(
            Paragraph("Terminal Cap Rate: ${Fmt.pct(inputs.terminalCapRate)}")
                .setFontSize(10f).setFontColor(BURGUNDY_DARK)
        )
        document.add(
            Paragraph("Terminal Value: ${Fmt.currency(result.terminalValue)}")
                .setFontSize(10f).setFontColor(BURGUNDY_DARK).setBold()
        )
        document.add(
            Paragraph("PV of Terminal Value: ${Fmt.currency(result.pvTerminalValue)}")
                .setFontSize(10f).setFontColor(BURGUNDY_DARK).setBold()
        )
    }

    private fun addAssumptions(document: Document, inputs: HotelInputs) {
        addSectionTitle(document, "KEY ASSUMPTIONS")

        val table = Table(UnitValue.createPercentArray(floatArrayOf(2f, 1f)))
            .useAllAvailableWidth()
            .setFontSize(10f)

        val assumptions = listOf(
            "Number of Rooms" to "${inputs.numberOfRooms}",
            "Base Year Occupancy" to Fmt.pct(inputs.occupancyRate),
            "Base Year ADR" to Fmt.currencyDetail(inputs.adr),
            "ADR Growth Rate" to Fmt.pct(inputs.adrGrowthRate),
            "Occupancy Growth" to "${Fmt.pct(inputs.occupancyGrowthRate)} pts/yr",
            "Expense Growth Rate" to Fmt.pct(inputs.expenseGrowthRate),
            "Discount Rate (WACC)" to Fmt.pct(inputs.discountRate),
            "Terminal Cap Rate" to Fmt.pct(inputs.terminalCapRate),
            "Holding Period" to "5 Years",
            "FF&E Reserve" to Fmt.pct(inputs.reserveForReplacementPct),
            "Management Fee" to Fmt.pct(inputs.managementFeePct),
            "Franchise Fee" to Fmt.pct(inputs.franchiseFeePct),
        )

        assumptions.forEachIndexed { index, (label, value) ->
            addValRow(table, label, value, index % 2 == 1)
        }

        document.add(table)

        document.add(Paragraph("\n\n"))
        addDecoDivider(document)
        document.add(Paragraph("\n"))

        document.add(
            Paragraph("DISCLAIMER")
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(8f)
                .setFontColor(RICH_RED)
                .setCharacterSpacing(2f)
        )
        document.add(
            Paragraph(
                "This valuation analysis is prepared for informational purposes only and does not constitute " +
                "an appraisal or a guarantee of value. Actual results may vary materially from the projections " +
                "contained herein. The analysis is based on assumptions provided and market conditions as of the " +
                "date of preparation. No warranty is made regarding the accuracy or completeness of the information."
            )
                .setTextAlignment(TextAlignment.CENTER)
                .setFontSize(8f)
                .setFontColor(BURGUNDY)
                .setMarginLeft(30f)
                .setMarginRight(30f)
        )
    }

    // ── Helper methods for PDF formatting ──

    private fun addSectionTitle(document: Document, title: String) {
        addDecoDivider(document)
        document.add(
            Paragraph(title)
                .setFontSize(16f)
                .setFontColor(BURGUNDY_DARK)
                .setBold()
                .setCharacterSpacing(3f)
                .setTextAlignment(TextAlignment.CENTER)
                .setMarginTop(10f)
                .setMarginBottom(5f)
        )
        addDecoDivider(document)
        document.add(Paragraph("\n"))
    }

    private fun addSubSectionTitle(document: Document, title: String) {
        document.add(
            Paragraph(title)
                .setFontSize(11f)
                .setFontColor(RICH_RED)
                .setBold()
                .setCharacterSpacing(2f)
                .setMarginTop(10f)
                .setMarginBottom(8f)
        )
    }

    private fun addDecoDivider(document: Document) {
        val line = SolidLine(1f)
        line.color = ROSE_GOLD
        document.add(
            LineSeparator(line)
                .setMarginTop(5f)
                .setMarginBottom(5f)
        )
    }

    private fun addTableHeader(table: Table, vararg headers: String) {
        headers.forEach { header ->
            table.addHeaderCell(
                Cell()
                    .setBackgroundColor(BURGUNDY)
                    .setBorder(SolidBorder(ROSE_GOLD, 0.5f))
                    .setPadding(6f)
                    .add(
                        Paragraph(header)
                            .setFontSize(9f)
                            .setFontColor(CHAMPAGNE)
                            .setBold()
                            .setTextAlignment(if (header.isEmpty()) TextAlignment.LEFT else TextAlignment.RIGHT)
                            .setCharacterSpacing(1f)
                    )
            )
        }
    }

    private fun addTableRow(table: Table, label: String, val1: String, val2: String, alt: Boolean) {
        val bg = if (alt) TABLE_ALT else DARK_TABLE
        table.addCell(cellWith(label, bg, TextAlignment.LEFT))
        table.addCell(cellWith(val1, bg, TextAlignment.RIGHT))
        table.addCell(cellWith(val2, bg, TextAlignment.RIGHT))
    }

    private fun addValRow(table: Table, label: String, value: String, alt: Boolean) {
        val bg = if (alt) TABLE_ALT else DARK_TABLE
        table.addCell(cellWith(label, bg, TextAlignment.LEFT))
        table.addCell(cellWith(value, bg, TextAlignment.RIGHT, bold = true))
    }

    private fun addGroupHeader(table: Table, title: String, cols: Int) {
        table.addCell(
            Cell(1, cols)
                .setBackgroundColor(BURGUNDY)
                .setBorder(SolidBorder(ROSE_GOLD, 0.5f))
                .setPadding(5f)
                .add(
                    Paragraph(title)
                        .setFontSize(8f)
                        .setFontColor(ROSE_GOLD)
                        .setBold()
                        .setCharacterSpacing(2f)
                )
        )
    }

    private fun addProFormaRow(table: Table, label: String, values: List<String>, alt: Boolean) {
        val bg = if (alt) TABLE_ALT else DARK_TABLE
        table.addCell(cellWith(label, bg, TextAlignment.LEFT))
        values.forEach { v -> table.addCell(cellWith(v, bg, TextAlignment.RIGHT)) }
    }

    private fun addProFormaTotalRow(table: Table, label: String, values: List<String>) {
        table.addCell(
            Cell()
                .setBackgroundColor(BURGUNDY)
                .setBorderTop(SolidBorder(ROSE_GOLD, 1f))
                .setBorderBottom(SolidBorder(ROSE_GOLD, 1f))
                .setBorderLeft(SolidBorder(ROSE_GOLD, 0.5f))
                .setBorderRight(Border.NO_BORDER)
                .setPadding(5f)
                .add(
                    Paragraph(label)
                        .setFontSize(9f)
                        .setFontColor(CHAMPAGNE)
                        .setBold()
                )
        )
        values.forEach { v ->
            table.addCell(
                Cell()
                    .setBackgroundColor(BURGUNDY)
                    .setBorderTop(SolidBorder(ROSE_GOLD, 1f))
                    .setBorderBottom(SolidBorder(ROSE_GOLD, 1f))
                    .setBorderLeft(Border.NO_BORDER)
                    .setBorderRight(Border.NO_BORDER)
                    .setPadding(5f)
                    .add(
                        Paragraph(v)
                            .setFontSize(9f)
                            .setFontColor(CHAMPAGNE)
                            .setBold()
                            .setTextAlignment(TextAlignment.RIGHT)
                    )
            )
        }
    }

    private fun cellWith(
        text: String,
        bg: DeviceRgb,
        align: TextAlignment,
        bold: Boolean = false,
    ): Cell {
        return Cell()
            .setBackgroundColor(bg)
            .setBorder(SolidBorder(DeviceRgb(80, 30, 35), 0.25f))
            .setPadding(5f)
            .add(
                Paragraph(text)
                    .setFontSize(9f)
                    .setFontColor(IVORY)
                    .setTextAlignment(align)
                    .apply { if (bold) setBold() }
            )
    }
}
