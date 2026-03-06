package com.hotelvaluation

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.core.content.FileProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.hotelvaluation.export.PdfReportGenerator
import com.hotelvaluation.ui.HotelValuationViewModel
import com.hotelvaluation.ui.screens.*
import com.hotelvaluation.ui.theme.HotelValuationTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            HotelValuationTheme {
                val vm: HotelValuationViewModel = viewModel()
                val inputs by vm.inputs.collectAsState()
                val result by vm.result.collectAsState()
                val navController = rememberNavController()

                NavHost(navController = navController, startDestination = "dashboard") {
                    composable("dashboard") {
                        DashboardScreen(
                            inputs = inputs,
                            result = result,
                            onNavigate = { route -> navController.navigate(route) },
                            onExportPdf = { exportReport(vm) },
                        )
                    }
                    composable("inputs") {
                        InputsScreen(
                            inputs = inputs,
                            result = result,
                            vm = vm,
                            onBack = { navController.popBackStack() },
                        )
                    }
                    composable("growth") {
                        GrowthScreen(
                            inputs = inputs,
                            result = result,
                            vm = vm,
                            onBack = { navController.popBackStack() },
                        )
                    }
                    composable("pip") {
                        PipScreen(
                            inputs = inputs,
                            result = result,
                            vm = vm,
                            onBack = { navController.popBackStack() },
                        )
                    }
                    composable("proforma") {
                        ProFormaScreen(
                            result = result,
                            onBack = { navController.popBackStack() },
                        )
                    }
                    composable("dcf") {
                        DCFScreen(
                            inputs = inputs,
                            result = result,
                            onBack = { navController.popBackStack() },
                        )
                    }
                }
            }
        }
    }

    private fun exportReport(vm: HotelValuationViewModel) {
        try {
            val file = PdfReportGenerator.generate(
                context = this,
                inputs = vm.inputs.value,
                result = vm.result.value,
            )

            val uri = FileProvider.getUriForFile(
                this,
                "${packageName}.fileprovider",
                file,
            )

            val intent = Intent(Intent.ACTION_VIEW).apply {
                setDataAndType(uri, "application/pdf")
                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
            }

            val shareIntent = Intent.createChooser(intent, "View Hotel Valuation Report")
            startActivity(shareIntent)
        } catch (e: Exception) {
            Toast.makeText(this, "Error generating report: ${e.message}", Toast.LENGTH_LONG).show()
        }
    }
}
