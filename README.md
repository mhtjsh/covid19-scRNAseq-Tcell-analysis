# Decoding Immune Signatures in Post-Acute COVID-19 Lung Sequelae
### Project Overview

This project investigates the persistent immune alterations in the lungs of COVID-19 survivors by analyzing single-cell RNA sequencing (scRNA-seq) data. Building on the findings from the original study, "Immune signatures underlying post-acute COVID-19 lung sequelae", this analysis identifies and interprets the functional significance of differentially expressed genes (DEGs) to characterize the immune cell populations associated with post-acute COVID-19 complications.

The primary goal is to move beyond simple gene lists to understand the biological pathways that remain dysregulated in convalescent patients, contributing to a deeper understanding of Post-Acute Sequelae of COVID-19 (PASC).

### Analysis Pipeline

The computational analysis was performed using the R-based Seurat package. The complete, commented code and step-by-step implementation details can be found in the

`Covid19 Patients Data analysis whole.ipynb` notebook. Due to the high computational demand of the integration and normalization steps, the analysis was executed on a **Google Cloud Console VM**.

The high-level workflow included:

1.  **Data Loading & Quality Control:** Filtering of low-quality cells from the raw count matrices.
    
2.  **Normalization & Integration:** Normalization via `SCTransform` and integration using Seurat's anchor-based workflow to correct for technical batch effects across the 7 unique patient samples.
    
3.  **Dimensionality Reduction & Clustering:** PCA and UMAP for visualization, followed by graph-based clustering to identify distinct cell populations.
    
4.  **Differential Gene Expression & Functional Analysis:** Identification of DEGs between conditions and clusters, followed by Gene Ontology (GO) and pathway analysis to determine their biological significance.

### **Results & Discussion**

The analysis successfully identified significant differences between the immune cell profiles of healthy donors and convalescent COVID-19 patients. The following sections detail the progressive steps of dimensionality reduction, visualization, and functional interpretation.

#### **Principal Component Analysis (PCA) and Dimensionality**

After data integration, Principal Component Analysis (PCA) was performed to reduce the high-dimensional gene expression data into its most significant components of variation.

The **elbow plot** below visualizes the standard deviation of each principal component (PC). We use this plot to select the number of significant PCs to include in downstream analysis, typically choosing the point where the variance explained begins to plateau (the "elbow"). This ensures we capture the majority of the biological signal while excluding technical noise present in higher-dimension PCs.

A PCA plot provides a linear, two-dimensional representation of the data based on the first two principal components. This plot offers an initial glimpse into the data's structure, showing how cells cluster based on the greatest sources of variance.

<p align="center">
    <img width="700" height="450" alt="pca and elbow plots" src="https://github.com/user-attachments/assets/87bf9c6f-9609-4b36-8186-b89eef0143f9" />
    </br>
    <em><strong>Figure:</strong></em> The elbow plot above led us to use <strong>10 PCs</strong> in our downstream analysis, as these seemed to explain most of the variance in the data. 
  Plotting the data along the axes of the first two principal components showed significant separation between healthy and COVID-19 convalescent (diseased) groups. 
  Seurat-determined clusters revealed less distinct separation.
</p>


#### **Cellular Heterogeneity and Immune State**

Visualization of the integrated dataset via UMAP reveals a clear separation of cells based on disease status, indicating a profound and persistent transcriptomic shift in the immune cells of post-COVID patients.

<p align="center">
    <img width="700" height="450" alt="umap and heat map diseased and healthy" src="https://github.com/user-attachments/assets/7972d145-69de-44c2-88d5-95a96354845d" />
    </br>
    <em><strong>Figure:</strong></em>  To the left is a UMAP of our integrated dataset, grouped by status as healthy or COVID-19
convalescent(diseased), which leaves clear distinction between groups. To the right is a heat map of
the top 10 DEGs in each group.
</p>
