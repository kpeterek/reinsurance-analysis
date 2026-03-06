package com.hotelvaluation.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

// ── Financial Times Burgundy & Red Palette ──────────────────────────────────

val Burgundy900   = Color(0xFF1A0A0A)  // Deepest background
val Burgundy800   = Color(0xFF2D1114)  // Card backgrounds
val Burgundy700   = Color(0xFF4A1A20)  // Elevated surfaces
val Burgundy600   = Color(0xFF6B2530)  // Secondary containers
val Burgundy500   = Color(0xFF8B3040)  // Primary variant
val RichRed       = Color(0xFFA23B48)  // Primary brand color
val CrimsonAccent = Color(0xFFCC4455)  // Accent / interactive
val RoseGold      = Color(0xFFD4A574)  // Gold accent (art deco)
val ChampagneGold = Color(0xFFE8D5B5)  // Light gold
val Cream         = Color(0xFFFAF3E8)  // Text on dark
val IvoryWhite    = Color(0xFFFFF8F0)  // Bright text
val SlateGray     = Color(0xFF8A8A8A)  // Muted text
val DeepCharcoal  = Color(0xFF1E1E1E)  // Neutral dark
val ErrorRed      = Color(0xFFFF6B6B)
val PositiveGreen = Color(0xFF4CAF7D)

private val DarkColorScheme = darkColorScheme(
    primary = RichRed,
    onPrimary = IvoryWhite,
    primaryContainer = Burgundy600,
    onPrimaryContainer = ChampagneGold,
    secondary = RoseGold,
    onSecondary = Burgundy900,
    secondaryContainer = Burgundy700,
    onSecondaryContainer = ChampagneGold,
    tertiary = CrimsonAccent,
    onTertiary = IvoryWhite,
    background = Burgundy900,
    onBackground = Cream,
    surface = Burgundy800,
    onSurface = Cream,
    surfaceVariant = Burgundy700,
    onSurfaceVariant = ChampagneGold,
    outline = Burgundy500,
    error = ErrorRed,
    onError = Burgundy900,
)

@Composable
fun HotelValuationTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColorScheme,
        typography = HotelTypography,
        content = content,
    )
}
