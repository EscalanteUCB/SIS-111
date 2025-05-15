function ejecutarBusqueda() {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  hoja.clear(); // Limpiar hoja

  const cantidad = 30;
  const valorBuscado = 42;
  const tipoBusqueda = 'binaria'; // Cambia a 'lineal' si quieres usar esa

  // Generar lista ordenada de números aleatorios únicos
  const lista = generarListaUnicaOrdenada(cantidad);
  hoja.getRange(1, 1, lista.length, 1).setValues(lista.map(v => [v]));
  hoja.getRange(1, 2).setValue("Valor Buscado: " + valorBuscado);

  const tiempoInicio = new Date().getTime();
  let indice = -1;

  if (tipoBusqueda === 'lineal') {
    indice = busquedaLineal(lista, valorBuscado);
  } else {
    indice = busquedaBinaria(lista, valorBuscado);
  }

  const tiempoFin = new Date().getTime();
  const duracion = tiempoFin - tiempoInicio;

  if (indice >= 0) {
    hoja.getRange(indice + 1, 3).setValue("🔍 Encontrado");
  } else {
    hoja.getRange(1, 3).setValue("❌ Valor no encontrado");
  }

  hoja.getRange(2, 2).setValue("⏱ Tiempo: " + duracion + " ms");
}

function generarListaUnicaOrdenada(cantidad) {
  const set = new Set();
  while (set.size < cantidad) {
    set.add(Math.floor(Math.random() * cantidad * 3));
  }
  return Array.from(set).sort((a, b) => a - b);
}

function busquedaLineal(lista, valor) {
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === valor) return i;
  }
  return -1;
}

function busquedaBinaria(lista, valor) {
  let izq = 0, der = lista.length - 1;
  while (izq <= der) {
    let medio = Math.floor((izq + der) / 2);
    if (lista[medio] === valor) return medio;
    else if (lista[medio] < valor) izq = medio + 1;
    else der = medio - 1;
  }
  return -1;
}
