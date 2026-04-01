# Hospital Billing & Patient Report
This project is an end-to-end automation of 55,000+ patient records, transforming raw Excel data into **a live-sync Power BI environment**. 

## Project Workflow
- **Data Cleaning (Automated ETL Pipeline with Power Query):** Table Conversion, Deduplication, Text Scrubbing (string normalization, including whitespace trimming, case correction, and character replacement), and Data Type Standardization (Currency, Dates).
- **Data Quality check (Excel):**: Data Validation constraints with custom Error Alerts to prevent upstream data entry errors.
- **Cloud-Based Connection (Teams):** Linked Excel source via SharePoint/Teams from the start for an automated workflow.
- **Data Architecture (Excel & Power Bi):** Star Schema construction (References) and Relationships establishment (Model View)
- **Advanced Analytics & Visual Design (Power Bi):** DAX measures, calculate columns, custom theme from scratch, visualizations and filters.
- **Deployment & Distribution: (Power Bi Service)** Published to Power BI Service with Automated Scheduled Refresh enabled to recreate a realistic, hands-off business scenario.
  
> [!Note]
> This Power BI report is live-synced to a **private** SharePoint source.
> To view data locally:
> 1. Open Power BI Desktop.
> 2. Go to **File > Options and settings > Data source settings**.
> 3. Select **Change Source** and browse to the Excel file in this repository.

## Key technical features:
- **Cloud-Synced Data Source:** Excel file hosted in SharePoint/Teams to bypass local drive dependencies and enable cloud-to-cloud updates.
- **Automated Refresh Logic:** Set up a Scheduled Refresh in Power BI Service to demonstrate real-time data maintenance in a production environment.
- **Relational Data Modeling:** Implemented Star Schema to optimize DAX performance and ensure accurate cross-filtering between different tables.
- **Proactive Validation:** Built-in Excel constraints to ensure data integrity before it reaches the visualization stage.

## Security Considerations

This project uses a practice dataset with no real patient information. In a real-world scenario, sensitive healthcare data would require:

- **Row-Level Security (RLS):** to restrict access to patient data by role.
- **Object level security:** to control access to specific tables and columns.
- **Workspace & App Permissions:** to control who can view or edit reports.
- **Data Source Security:** to ensure only authorized users can access cloud sources like SharePoint/Teams.

## Data Source
The dataset used in this project is the [Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset/data) from Kaggle, consisting of 55,000+ patient records including clinical and financial information.
