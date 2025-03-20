# Generación de Facturas en PDF a partir de Archivos Excel

Este proyecto utiliza Python y la biblioteca FPDF para generar archivos PDF a partir de datos contenidos en archivos de Excel (.xlsx). El script lee varias facturas desde un directorio especificado (`invoices/`), extrae información clave como el número de factura y la fecha desde el nombre del archivo, y luego crea un archivo PDF con esos datos, junto con un formato básico para cada factura.

### Funcionalidades:
- **Lectura de archivos Excel**: El script recorre los archivos `.xlsx` en el directorio `invoices/` y extrae la información de la primera hoja de cada archivo.
- **Generación de PDF**: Para cada archivo Excel, se crea un documento PDF con el número de factura y la fecha en el encabezado. Cada factura se guarda como un archivo PDF individual.
- **Personalización de formato**: El número de factura y la fecha son destacados con una fuente en negrita y un tamaño adecuado, con el resto del contenido formateado y guardado como PDF.

Este proyecto es útil para generar facturas o informes a partir de archivos Excel, convirtiéndolos automáticamente en documentos PDF organizados por nombre de archivo.

Los archivos PDF generados se guardan en la carpeta `pdf_invoices`.
