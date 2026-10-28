# Data availability and provenance

The project includes `marajo_data.xyz`, as provided by the manuscript author. The file is not a complete inventory of all inputs referenced in the research notebooks. Its coordinate reference system, unit conventions, original provider, processing lineage, and redistribution terms must be confirmed by the authors before submission.

Some geographical notebooks reference external Shapefile bundles and machine-specific absolute paths. Those inputs are **not included** in this release. To reproduce these notebooks independently, the authors must supply or point to accessible sources for all needed `.shp`, `.shx`, `.dbf`, `.prj`, and any other files, then convert absolute paths to project-relative paths.

Do not state that all manuscript figures or geological interpretations have been reproduced from this release; that has not yet been established. The deterministic Python test suite and standalone synthetic example are the presently verified workflows.
