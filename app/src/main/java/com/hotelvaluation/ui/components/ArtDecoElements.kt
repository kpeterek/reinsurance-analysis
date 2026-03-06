package com.hotelvaluation.ui.components

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import com.hotelvaluation.ui.theme.*

/**
 * Art Deco decorative divider with geometric fan pattern.
 */
@Composable
fun ArtDecoDivider(
    modifier: Modifier = Modifier,
    color: Color = RoseGold,
) {
    Canvas(
        modifier = modifier
            .fillMaxWidth()
            .height(24.dp)
            .padding(horizontal = 32.dp)
    ) {
        val centerX = size.width / 2
        val centerY = size.height / 2

        // Center diamond
        val diamondSize = 6f
        val diamondPath = Path().apply {
            moveTo(centerX, centerY - diamondSize)
            lineTo(centerX + diamondSize, centerY)
            lineTo(centerX, centerY + diamondSize)
            lineTo(centerX - diamondSize, centerY)
            close()
        }
        drawPath(diamondPath, color)

        // Lines extending from diamond
        val lineGap = 12f
        drawLine(
            color = color,
            start = Offset(centerX - diamondSize - lineGap, centerY),
            end = Offset(40f, centerY),
            strokeWidth = 1.5f,
            cap = StrokeCap.Round,
        )
        drawLine(
            color = color,
            start = Offset(centerX + diamondSize + lineGap, centerY),
            end = Offset(size.width - 40f, centerY),
            strokeWidth = 1.5f,
            cap = StrokeCap.Round,
        )

        // Small decorative ticks
        for (i in 1..3) {
            val offset = diamondSize + lineGap + 15f + (i * 20f)
            val tickHeight = (4 - i) * 2f
            drawLine(color, Offset(centerX - offset, centerY - tickHeight), Offset(centerX - offset, centerY + tickHeight), 1.5f)
            drawLine(color, Offset(centerX + offset, centerY - tickHeight), Offset(centerX + offset, centerY + tickHeight), 1.5f)
        }
    }
}

/**
 * Burgundy card with gold border accent — the primary container for content.
 */
@Composable
fun ValuationCard(
    modifier: Modifier = Modifier,
    title: String? = null,
    content: @Composable ColumnScope.() -> Unit,
) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(
                Brush.verticalGradient(
                    colors = listOf(Burgundy800, Burgundy800.copy(alpha = 0.95f))
                )
            )
            .padding(1.dp)
    ) {
        if (title != null) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(
                        Brush.horizontalGradient(
                            colors = listOf(
                                Burgundy700,
                                Burgundy600.copy(alpha = 0.6f),
                                Burgundy700,
                            )
                        )
                    )
                    .padding(horizontal = 16.dp, vertical = 10.dp)
            ) {
                Text(
                    text = title.uppercase(),
                    style = MaterialTheme.typography.labelLarge,
                    letterSpacing = MaterialTheme.typography.labelLarge.letterSpacing,
                )
            }
        }
        Column(
            modifier = Modifier.padding(16.dp),
            content = content,
        )
    }
}

/**
 * Prominent valuation figure display with large serif number.
 */
@Composable
fun ValuationFigure(
    label: String,
    value: String,
    modifier: Modifier = Modifier,
    valueColor: Color = ChampagneGold,
    subtext: String? = null,
) {
    Column(
        modifier = modifier,
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Text(
            text = label.uppercase(),
            style = MaterialTheme.typography.labelMedium,
            textAlign = TextAlign.Center,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = value,
            style = MaterialTheme.typography.displayMedium.copy(
                color = valueColor,
                fontWeight = FontWeight.Bold,
            ),
            textAlign = TextAlign.Center,
        )
        if (subtext != null) {
            Text(
                text = subtext,
                style = MaterialTheme.typography.bodySmall,
                textAlign = TextAlign.Center,
            )
        }
    }
}

/**
 * Horizontal line item row for pro forma tables.
 */
@Composable
fun LineItemRow(
    label: String,
    values: List<String>,
    modifier: Modifier = Modifier,
    isHeader: Boolean = false,
    isTotal: Boolean = false,
    labelColor: Color = if (isHeader) RoseGold else Cream,
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .then(
                if (isTotal) Modifier.background(Burgundy700.copy(alpha = 0.5f)) else Modifier
            )
            .padding(vertical = 6.dp, horizontal = 8.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = if (isHeader) label.uppercase() else label,
            style = if (isHeader || isTotal)
                MaterialTheme.typography.bodyMedium.copy(fontWeight = FontWeight.SemiBold, color = labelColor)
            else
                MaterialTheme.typography.bodyMedium,
            modifier = Modifier.weight(1.4f),
        )
        values.forEach { value ->
            Text(
                text = value,
                style = if (isTotal)
                    MaterialTheme.typography.bodyMedium.copy(fontWeight = FontWeight.Bold, color = ChampagneGold)
                else
                    MaterialTheme.typography.bodyMedium,
                textAlign = TextAlign.End,
                modifier = Modifier.weight(1f),
            )
        }
    }
}

/**
 * Section header with art deco styling.
 */
@Composable
fun SectionHeader(
    title: String,
    modifier: Modifier = Modifier,
) {
    Column(modifier = modifier.fillMaxWidth()) {
        Spacer(modifier = Modifier.height(16.dp))
        Text(
            text = title,
            style = MaterialTheme.typography.headlineMedium,
        )
        Spacer(modifier = Modifier.height(4.dp))
        ArtDecoDivider()
        Spacer(modifier = Modifier.height(8.dp))
    }
}
