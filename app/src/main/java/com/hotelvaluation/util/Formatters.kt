package com.hotelvaluation.util

import java.text.NumberFormat
import java.util.Locale

object Fmt {
    private val currencyFmt = NumberFormat.getCurrencyInstance(Locale.US).apply {
        maximumFractionDigits = 0
    }
    private val currencyDetailFmt = NumberFormat.getCurrencyInstance(Locale.US).apply {
        maximumFractionDigits = 2
    }
    private val pctFmt = NumberFormat.getPercentInstance(Locale.US).apply {
        minimumFractionDigits = 1
        maximumFractionDigits = 1
    }
    private val numberFmt = NumberFormat.getNumberInstance(Locale.US).apply {
        maximumFractionDigits = 0
    }
    private val decimalFmt = NumberFormat.getNumberInstance(Locale.US).apply {
        minimumFractionDigits = 2
        maximumFractionDigits = 2
    }

    fun currency(value: Double): String = currencyFmt.format(value)
    fun currencyDetail(value: Double): String = currencyDetailFmt.format(value)
    fun pct(value: Double): String = pctFmt.format(value)
    fun number(value: Double): String = numberFmt.format(value)
    fun decimal(value: Double): String = decimalFmt.format(value)
    fun multiplier(value: Double): String = "${decimal(value)}x"

    fun compactCurrency(value: Double): String {
        return when {
            value >= 1_000_000_000 -> "$${decimalFmt.format(value / 1_000_000_000)}B"
            value >= 1_000_000 -> "$${decimalFmt.format(value / 1_000_000)}M"
            value >= 1_000 -> "$${decimalFmt.format(value / 1_000)}K"
            else -> currency(value)
        }
    }
}

fun String.toDoubleOrDefault(default: Double = 0.0): Double {
    return this.toDoubleOrNull() ?: default
}

fun Double.toPctInput(): String {
    return if (this == 0.0) "" else (this * 100).let {
        if (it == it.toLong().toDouble()) it.toLong().toString() else "%.1f".format(it)
    }
}

fun String.fromPctInput(): Double {
    return (this.toDoubleOrNull() ?: 0.0) / 100.0
}

fun Double.toDollarInput(): String {
    return if (this == 0.0) "" else {
        if (this == this.toLong().toDouble()) this.toLong().toString()
        else "%.2f".format(this)
    }
}

fun Double.toIntInput(): String {
    return if (this == 0.0) "" else this.toInt().toString()
}
