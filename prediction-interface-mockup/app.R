#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Car Service Predictions"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
         selectInput("EC", label = "Error Code", 
                     choices = list("E101" = 1, "E302" = 2, "E412" = 3,
                                    "E420" = 4, "E421" = 5, "E422" = 6,
                                    "E601" = 7, "Other" = 8), 
                     selected = 1),
         selectInput("make", label = "Make", 
                     choices = list("Chevrolet" = 1, "Dodge" = 2, "Ford" = 3,
                                    "GMC" = 4, "Honda" = 5, "Hyundai" = 6,
                                    "Lincoln" = 7, "Mercury" = 8, "Mitsubishi" = 9,
                                    "Nissan" = 10, "Suzuki" = 11, "Toyota" = 12,
                                    "Other" = 13), 
                     selected = 1),
         sliderInput("size", "Engine Size (L):",
                     min = 1, max = 10,
                     value = 3.2, step = 0.1),
         selectInput("fuel", label = "Fuel Type", 
                     choices = list("Diesel" = 1, "Electric" = 2, "Flexfuel" = 3,
                                    "Gas" = 4, "Hybrid" = 5),
                     selected = 1),
         sliderInput("mileage", "Mileage",
                     min = 0, max = 300000,
                     value = 50000),
         sliderInput("age", "Car Age",
                     min = 0, max = 25,
                     value = 5),
         dateInput("date", "Date:", value = "2017-12-04"),
         hr(),
         fluidRow(column(3, verbatimTextOutput("value")))
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot"),
         h3(textOutput("caption"))
      )
   )
)


# Define server logic required to draw a histogram
server <- function(input, output) {
  
   feat_mult <- function(size, mileage, age) {
    total <- size + mileage + age
    (size * input$size / 10 + mileage * input$mileage / 300000 + age * input$age / 25) / total
   }
   
   x <- c()
   
   output$distPlot <- renderPlot({
      # generate bins based on input$bins from ui.R
      x['bespoke'] <- feat_mult(1, 2, 4)
      x['nitro_fill'] <- feat_mult(4, 2, 4)
      x['multi_pt_insp'] <- feat_mult(8, 9, 10)
      x['filter'] <- feat_mult(1, 20, 1)
      x['batt_test'] <- feat_mult(0, 0, 1)
      x['repair_refinish'] <- feat_mult(1, 15, 1)
      x['change_oil'] <- feat_mult(5, 5, 5)
      x['safety_syst'] <- feat_mult(20, 1, 4)
      x['air_filter'] <- feat_mult(8, 2, 8)
      x['belts_hoses'] <- feat_mult(10, 11, 12)
      x['tire_inf'] <- feat_mult(19, 10, 5)
      x['haz_waste'] <- feat_mult(1, 20, 1)
      #x    <- faithful[, 2] 
      #bins <- seq(min(x), max(x), length.out = input$age + 1)
      
      # draw the histogram with the specified number of bins
      #hist(x, breaks = bins, col = 'darkgray', border = 'white')
      barplot(x, main = "Operation Likelihood", ylab = "Probablity", las = 2)
   })
   
   likelihood_check <- function(repair_refinish) {
     if (repair_refinish < .25) {
       "highly unlikely"
     } else if (repair_refinish < .5) {
       "unlikely"
     } else if (repair_refinish < .75) {
       "likely"
     } else {
       "highly likely"
     }
   }
   
   output$caption <- renderText({ paste("It is ", likelihood_check(feat_mult(1, 15, 1)), " (", round(100 * feat_mult(1, 15, 1), digits = 0), "%)", " that your car will need some repair or refinishing. Your dealership will reach out to you soon. If you do not hear from them within 7 days, please contact them.", sep = "") })
}

# Run the application 
shinyApp(ui = ui, server = server)

