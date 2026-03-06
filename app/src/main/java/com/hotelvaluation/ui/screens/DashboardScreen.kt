package com.hotelvaluation.ui.screens

import androidx.compose.animation.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.hotelvaluation.model.HotelInputs
import com.hotelvaluation.model.ValuationResult
import com.hotelvaluation.ui.components.*
import com.hotelvaluation.ui.theme.*
import com.hotelvaluation.util.Fmt

@Composable
fun DashboardScreen(
    inputs: HotelInputs,
    result: ValuationResult,
    onNavigate: (String) -> Unit,
    onExportPdf: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Burgundy900)
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
    ) {
        // ── Header ──
        Spacer(modifier = Modifier.height(8.dp))
        Text(
            text = "HOTEL VALUATION",
            style = MaterialTheme.typography.labelLarge.copy(
                letterSpacing = MaterialTheme.typography.labelLarge.letterSpacing,
            ),
            modifier = Modifier.fillMaxWidth(),
            textAlign = TextAlign.Center,
        )
        Text(
            text = inputs.propertyName,
            style = MaterialTheme.typography.displayLarge,
            modifier = Modifier.fillMaxWidth(),
            textAlign = TextAlign.Center,
        )
        ArtDecoDivider()

        Spacer(modifier = Modifier.height(16.dp))

        // ── Primary Valuation ──
        ValuationCard(title = "DCF Valuation") {
            ValuationFigure(
                label = "Total Property Value",
                value = Fmt.compactCurrency(result.totalPropertyValue),
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(modifier = Modifier.height(16.dp))
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly,
            ) {
                ValuationFigure(
                    label = "Value Per Room",
                    value = Fmt.compactCurrency(result.valuePerRoom),
                    modifier = Modifier.weight(1f),
                    valueColor = RoseGold,
                )
                ValuationFigure(
                    label = "Implied Cap Rate",
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

        // ── Key Metrics Row ──
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            MetricCard(
                label = "Year 1 NOI",
                value = Fmt.compactCurrency(result.yearProjections.firstOrNull()?.netOperatingIncome ?: 0.0),
                modifier = Modifier.weight(1f),
            )
            MetricCard(
                label = "Year 5 NOI",
                value = Fmt.compactCurrency(result.yearProjections.lastOrNull()?.netOperatingIncome ?: 0.0),
                modifier = Modifier.weight(1f),
            )
        }

        Spacer(modifier = Modifier.height(8.dp))

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            MetricCard(
                label = "Terminal Value",
                value = Fmt.compactCurrency(result.terminalValue),
                modifier = Modifier.weight(1f),
            )
            MetricCard(
                label = "PV Terminal",
                value = Fmt.compactCurrency(result.pvTerminalValue),
                modifier = Modifier.weight(1f),
            )
        }

        Spacer(modifier = Modifier.height(16.dp))

        // ── Property Snapshot ──
        ValuationCard(title = "Property Snapshot") {
            SnapshotRow("Rooms", "${inputs.numberOfRooms}")
            SnapshotRow("Occupancy", Fmt.pct(inputs.occupancyRate))
            SnapshotRow("ADR", Fmt.currencyDetail(inputs.adr))
            SnapshotRow("RevPAR", Fmt.currencyDetail(inputs.occupancyRate * inputs.adr))
            SnapshotRow("Discount Rate", Fmt.pct(inputs.discountRate))
            SnapshotRow("Terminal Cap Rate", Fmt.pct(inputs.terminalCapRate))
            if (inputs.pipEnabled) {
                SnapshotRow("PIP Budget", Fmt.currency(inputs.pipTotalCost))
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        // ── Navigation Buttons ──
        SectionHeader(title = "Analysis")

        NavButton("Property & Revenue Inputs", Icons.Filled.Hotel) { onNavigate("inputs") }
        NavButton("Growth Assumptions", Icons.Filled.TrendingUp) { onNavigate("growth") }
        NavButton("Property Improvement Plan", Icons.Filled.Build) { onNavigate("pip") }
        NavButton("5-Year Pro Forma", Icons.Filled.TableChart) { onNavigate("proforma") }
        NavButton("DCF Analysis", Icons.Filled.Assessment) { onNavigate("dcf") }

        Spacer(modifier = Modifier.height(16.dp))

        // ── Export Button ──
        Button(
            onClick = onExportPdf,
            modifier = Modifier
                .fillMaxWidth()
                .height(56.dp),
            colors = ButtonDefaults.buttonColors(
                containerColor = RichRed,
                contentColor = IvoryWhite,
            ),
            shape = RoundedCornerShape(8.dp),
        ) {
            Icon(Icons.Filled.PictureAsPdf, contentDescription = null)
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                "EXPORT FULL REPORT",
                style = MaterialTheme.typography.labelLarge.copy(color = IvoryWhite),
            )
        }

        Spacer(modifier = Modifier.height(32.dp))
    }
}

@Composable
private fun MetricCard(
    label: String,
    value: String,
    modifier: Modifier = Modifier,
) {
    Box(
        modifier = modifier
            .clip(RoundedCornerShape(8.dp))
            .background(
                Brush.verticalGradient(
                    listOf(Burgundy700, Burgundy800)
                )
            )
            .padding(16.dp),
    ) {
        Column {
            Text(
                text = label.uppercase(),
                style = MaterialTheme.typography.labelMedium,
            )
            Spacer(modifier = Modifier.height(4.dp))
            Text(
                text = value,
                style = MaterialTheme.typography.headlineSmall.copy(
                    color = ChampagneGold,
                    fontWeight = FontWeight.Bold,
                ),
            )
        }
    }
}

@Composable
private fun SnapshotRow(label: String, value: String) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
    ) {
        Text(text = label, style = MaterialTheme.typography.bodyMedium)
        Text(
            text = value,
            style = MaterialTheme.typography.bodyMedium.copy(
                fontWeight = FontWeight.SemiBold,
                color = ChampagneGold,
            ),
        )
    }
}

@Composable
private fun NavButton(
    label: String,
    icon: ImageVector,
    onClick: () -> Unit,
) {
    OutlinedButton(
        onClick = onClick,
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        colors = ButtonDefaults.outlinedButtonColors(
            contentColor = Cream,
        ),
        border = ButtonDefaults.outlinedButtonBorder.copy(
            brush = Brush.horizontalGradient(listOf(Burgundy500, RichRed, Burgundy500))
        ),
        shape = RoundedCornerShape(8.dp),
    ) {
        Icon(icon, contentDescription = null, tint = RoseGold, modifier = Modifier.size(20.dp))
        Spacer(modifier = Modifier.width(12.dp))
        Text(label, modifier = Modifier.weight(1f))
        Icon(Icons.Filled.ChevronRight, contentDescription = null, tint = SlateGray)
    }
}
