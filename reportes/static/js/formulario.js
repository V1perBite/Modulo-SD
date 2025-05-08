document
  .getElementById("formularioReporte")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const formato = document.getElementById("formato").value;
    const tipo = document.getElementById("tipo_reporte").value;
    const inicio = document.getElementById("fecha_inicio").value;
    const fin = document.getElementById("fecha_fin").value;

    const url = `/reportes/api/reportes/?formato=${formato}&tipo_reporte=${tipo}&fecha_inicio=${inicio}&fecha_fin=${fin}`;

    const response = await fetch(url);

    if (response.ok) {
      const blob = await response.blob();
      const enlace = document.createElement("a");
      enlace.href = window.URL.createObjectURL(blob);
      enlace.download =
        formato === "excel" ? "productos.xlsx" : "productos.pdf";
      enlace.click();
    } else {
      const data = await response.json();
      alert("Error: " + (data.error || "Error al generar el reporte"));
    }
  });
