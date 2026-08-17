import * as XLSX from "xlsx";
import type { Clasificacion } from "./interfaces/IArticulo";
import { Clase } from "./models/Clase";
import { Familia } from "./models/Familia";
import { Producto } from "./models/Producto";
import { Segmento } from "./models/Segmento";

export function agruparFaltantes(list: Clasificacion[]) {
	const segmentos: Clasificacion[] = [];
	const familias: Clasificacion[] = [];
	const clases: Clasificacion[] = [];
	const productos: Clasificacion[] = [];
	const vacios: Clasificacion[] = [];
	list.forEach((cls) => {
		const grupo =
			cls.producto.eleccion instanceof Producto
				? productos
				: cls.clase.eleccion instanceof Clase
					? clases
					: cls.familia.eleccion instanceof Familia
						? familias
						: cls.segmento.eleccion instanceof Segmento
							? segmentos
							: vacios;
		grupo.push(cls);
	});
	return {
		segmentos,
		familias,
		clases,
		productos,
		vacios,
	};
}

export async function cargarExcel(
	event: Event,
): Promise<Array<{ [key: string]: any }>> {
	const input = event.currentTarget as HTMLInputElement;
	const file = input.files?.[0];

	if (!file) return [];

	const buffer = await file.arrayBuffer();

	const workbook = XLSX.read(buffer);

	const nombreHoja = workbook.SheetNames[0];
	const hoja = workbook.Sheets[nombreHoja];

	const datos: Array<{}> = XLSX.utils.sheet_to_json(hoja);

	return datos;
}