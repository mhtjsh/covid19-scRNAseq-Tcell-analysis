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
    <em><strong>Figure:</strong></em> To the left is a UMAP of our integrated dataset, grouped by status as healthy or COVID-19
convalescent(diseased), which leaves clear distinction between groups. To the right is a heat map of
the top 10 DEGs in each group.
</p>

Further clustering identified multiple distinct cell populations, suggesting significant cellular heterogeneity within the T-cell compartment of the lung.

<p align="center">
    <img width="700" height="450" alt="umap and heatmap clusters" src="https://github.com/user-attachments/assets/cc8cdc23-eeab-406a-a9bf-c53a0eab4f91" />
    </br>
    <em><strong>Figure:</strong></em> To the left is a UMAP of our integrated dataset, grouped by Seurat-determined clusters. To
the right is a heat map of the top 5 DEGs in each cluster.
</p>

#### **Differential Gene Expression Highlights a Pro-Inflammatory Environment**

To understand the molecular basis for the separation observed in the UMAP plots, we performed differential gene expression analysis. The heatmap below shows the top 10 genes that distinguish the "COVID\_Recovery" and "Healthy" groups. The expression pattern points towards a sustained inflammatory state in the convalescent group.

Similarly, identifying marker genes for each cell cluster revealed unique gene signatures, which are visualized in the following heatmap.

#### **Functional Enrichment Analysis Reveals Sustained Immune Activation**

The core of this project's outcome lies in the functional analysis of the differentially expressed genes. By performing Gene Ontology (GO) and pathway analysis (detailed results available in `report.pdf` and `result.csv`), we can interpret the biological meaning behind the long lists of DEGs.

My analysis revealed that the genes upregulated in convalescent COVID-19 patients are significantly enriched in pathways associated with:

*   **T-Cell Activation and Cytotoxicity:** Terms such as "T cell activation," "leukocyte mediated cytotoxicity," and "natural killer cell mediated cytotoxicity" were highly significant. This suggests that cytotoxic T-cells remain in a heightened state of alert long after the initial infection has cleared, which could contribute to chronic tissue damage in the lungs.
    
*   **Interferon Signaling:** A strong enrichment for "response to interferon-gamma" and "type I interferon signaling pathway" was observed. Interferons are critical for antiviral defense, but their prolonged expression is a hallmark of many chronic inflammatory and autoimmune conditions. This sustained interferon signature is a key indicator of an immune system that has failed to return to homeostasis.
    
*   **Inflammatory Response:** General inflammatory pathways, including "inflammatory response" and "cytokine-mediated signaling pathway," were also prominent. This points to a broad, non-specific inflammatory environment persisting in the lungs of post-COVID patients.
    
These findings strongly suggest that the long-term sequelae of COVID-19 are not due to a failure to clear the virus, but rather to an immune system that has become "stuck" in a pro-inflammatory, antiviral state. This sustained activation, particularly of cytotoxic T-cells and interferon pathways, likely drives the chronic inflammation and impaired lung function seen in PASC.

Project Contributions and Future Directions
-------------------------------------------

### **Contributions of This Project**

This project serves as a focused re-analysis of the scRNA-seq data from the original paper, "Immune signatures underlying post-acute COVID-19 lung sequelae". While the original study performed a broad, multi-faceted investigation, this project deliberately narrows its scope to the bronchoalveolar lavage (BAL) T-cells to perform a more controlled and detailed comparison between healthy and convalescent individuals.

By employing a distinct and arguably more robust bioinformatic pipeline, this project not only validates the original findings but also contributes several new and more detailed insights:

1.  **Advanced Normalization and Analysis:** This project utilized a more advanced normalization method, **SCTransform**, which uses a regularized negative binomial regression model to more effectively remove technical variability from sequencing depth. This choice was made with the goal of reducing the rate of false positives and increasing the reliability of the downstream differential gene expression results. The clustering was performed using Seurat's SNN modularity optimization-based approach.
    
2.  **Identification of a Specific Inflammatory Signature:** A key new finding was the significant upregulation of pro-inflammatory genes like **IL32 and CCL5** in the cell clusters dominated by the COVID-19 recovery group. This points to a "consistent inflammatory response in the covid sequelae individuals," an aspect that was not explored in detail with the scRNA-seq data in the original publication. The clear separation of healthy and diseased cells in the UMAP plots provides strong visual support for this distinct transcriptomic state.
    
3.  **Detailed and Corroborated Pathway Analysis:** By leveraging two distinct databases, **Reactome and DAVID**, this project provides a more granular and well-corroborated view of the dysregulated pathways. While validating the original paper's findings of T-cell activation, this dual analysis offers more specific mechanistic details. For instance, Reactome highlighted the "phosphorylation of CD3 and TCR zeta chains," while DAVID pointed to "T cytotoxic cell surface molecules," both of which are critical upstream events in T-cell activation and proliferation.
    

In essence, this project acts as a valuable case study in how the re-analysis of publicly available data with alternative computational strategies can yield more detailed and novel biological insights, successfully building upon the foundational work of the original authors.

### **Future Directions**

Building on the foundation of this work, several exciting avenues for future research emerge:

*   **Granular Sub-Clustering:** The major T-cell lineages (CD4+, CD8+) can be isolated and re-clustered to identify more specific subtypes, such as effector memory, central memory, resident memory, and exhausted T-cells. Understanding which of these specific subsets are expanded or dysregulated in PASC is a critical next step.
    
*   **Cell-Cell Communication Modeling:** The current analysis treats cells as independent entities. A powerful next step would be to use tools like CellChat or NicheNet to model receptor-ligand interactions. This could reveal how different T-cell subsets are communicating with each other and with other lung cells, and how this communication network is rewired after COVID-19.
    
*   **Integration with T-Cell Receptor (TCR) Sequencing:** The original dataset contains paired TCR-seq data. Integrating our gene expression analysis with this TCR data would be a highly impactful step. This would allow us to link the functional state (transcriptome) of a T-cell with its antigen specificity (clonotype), answering questions like: "Are the most expanded T-cell clones also the ones showing the highest expression of cytotoxic or exhaustion markers?" This would provide a direct link between the adaptive immune response to the virus and the long-term functional state of the T-cells.

### Conclusion

This project successfully leveraged single-cell RNA sequencing data to decode the persistent immune signatures in patients recovering from COVID-19. By moving beyond DEG identification to functional pathway analysis, we have demonstrated that the post-acute phase is characterized by a sustained and specific pattern of immune dysregulation. The key takeaway is the **prolonged activation of cytotoxic T-cell and interferon-gamma signaling pathways**, which provides a compelling molecular explanation for the chronic inflammation and tissue damage underlying post-COVID lung sequelae.

These findings highlight potential therapeutic targets aimed at resolving this persistent inflammation and restoring immune homeostasis in patients suffering from the long-term effects of COVID-19.
