package com.hotelvaluation.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.hotelvaluation.ui.theme.*

/**
 * Styled currency/number input field with burgundy theme.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ValuationTextField(
    label: String,
    value: String,
    onValueChange: (String) -> Unit,
    modifier: Modifier = Modifier,
    prefix: String? = null,
    suffix: String? = null,
    isPercentage: Boolean = false,
    keyboardType: KeyboardType = KeyboardType.Decimal,
) {
    OutlinedTextField(
        value = value,
        onValueChange = { newValue ->
            // Allow only valid numeric input
            val filtered = newValue.filter { it.isDigit() || it == '.' || it == '-' }
            if (filtered.count { it == '.' } <= 1) {
                onValueChange(filtered)
            }
        },
        label = { Text(label, color = SlateGray) },
        modifier = modifier.fillMaxWidth(),
        singleLine = true,
        keyboardOptions = KeyboardOptions(keyboardType = keyboardType),
        prefix = prefix?.let {
            { Text(it, color = RoseGold) }
        },
        suffix = (suffix ?: if (isPercentage) "%" else null)?.let { s ->
            { Text(s, color = RoseGold) }
        },
        colors = OutlinedTextFieldDefaults.colors(
            focusedTextColor = IvoryWhite,
            unfocusedTextColor = Cream,
            cursorColor = CrimsonAccent,
            focusedBorderColor = RichRed,
            unfocusedBorderColor = Burgundy500,
            focusedLabelColor = RoseGold,
            unfocusedLabelColor = SlateGray,
            focusedContainerColor = Burgundy800,
            unfocusedContainerColor = Burgundy800.copy(alpha = 0.7f),
        ),
        shape = RoundedCornerShape(6.dp),
    )
}

/**
 * Input row with label and value field side by side.
 */
@Composable
fun InputRow(
    label: String,
    value: String,
    onValueChange: (String) -> Unit,
    modifier: Modifier = Modifier,
    prefix: String? = null,
    suffix: String? = null,
    isPercentage: Boolean = false,
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.bodyMedium,
            modifier = Modifier.weight(1.2f),
        )
        ValuationTextField(
            label = "",
            value = value,
            onValueChange = onValueChange,
            modifier = Modifier.weight(1f),
            prefix = prefix,
            suffix = suffix,
            isPercentage = isPercentage,
        )
    }
}

/**
 * Segmented button group for input mode selection.
 */
@Composable
fun InputModeSelector(
    selectedMode: String,
    onModeSelected: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    val modes = listOf("% Revenue", "PAR", "POR")
    Row(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(Burgundy800)
            .padding(2.dp),
        horizontalArrangement = Arrangement.SpaceEvenly,
    ) {
        modes.forEach { mode ->
            val isSelected = mode == selectedMode
            Box(
                modifier = Modifier
                    .weight(1f)
                    .clip(RoundedCornerShape(6.dp))
                    .background(if (isSelected) RichRed else Burgundy800)
                    .padding(vertical = 10.dp),
                contentAlignment = Alignment.Center,
            ) {
                Text(
                    text = mode,
                    style = MaterialTheme.typography.labelLarge.copy(
                        color = if (isSelected) IvoryWhite else SlateGray,
                    ),
                    textAlign = TextAlign.Center,
                    modifier = Modifier
                        .fillMaxWidth()
                        .noRippleClickable { onModeSelected(mode) },
                )
            }
        }
    }
}

/**
 * Switch with label for boolean toggles.
 */
@Composable
fun LabeledSwitch(
    label: String,
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit,
    modifier: Modifier = Modifier,
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.bodyLarge,
        )
        Switch(
            checked = checked,
            onCheckedChange = onCheckedChange,
            colors = SwitchDefaults.colors(
                checkedThumbColor = IvoryWhite,
                checkedTrackColor = RichRed,
                uncheckedThumbColor = SlateGray,
                uncheckedTrackColor = Burgundy700,
            ),
        )
    }
}
