import * as XLSX from "xlsx";
import type { Clasificacion } from "./interfaces/IArticulo";
import { Clase } from "./models/Clase";
import { Familia } from "./models/Familia";
import { Producto } from "./models/Producto";
import { Segmento } from "./models/Segmento";
import type { IAgrupacion } from "./interfaces/IAgrupacion";
import { API } from "./utils/fetchUtils";

export function agruparFaltantes(
	map: Record<string, Clasificacion>,
	orden: Set<string>,
): IAgrupacion {
	const segmentos = new Set<Clasificacion>();
	const familias = new Set<Clasificacion>();
	const clases = new Set<Clasificacion>();
	const productos = new Set<Clasificacion>();
	const vacios = new Set<Clasificacion>();
	const sinDescripcion = new Set<Clasificacion>();
	orden.forEach((id) => {
		if (!map?.[id]) return;
		const cls = map[id] as Clasificacion;
		if (cls.articulo.descripcion === "") sinDescripcion.add(cls);
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
		grupo.add(cls);
	});
	return {
		sinDescripcion,
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

export function getTestArticles() {
	return [
		{
			articulo: {
				id: "adwa",
				nombre: "Pollo a la brasa",
			},
			segmento: {
				motivo: "porque esta muy bonito",
				confianza: 0.9,
				eleccion: new Segmento("500000", "segmento", []),
			},
			familia: {
				eleccion: new Familia("", "familia"),
			},
			clase: {
				eleccion: new Clase("", "clase"),
			},
			producto: {
				eleccion: new Producto("", "producto"),
			},
		},
		...new Array(20).fill(null).map(() => {
			const min = 1;
			const max = 200;
			return {
				articulo: {
					id: "test-" + String(Math.floor(Math.random() * (max - min + 1))),
					nombre: "Tallarin saltado",
					descripcion: "nose que poner aa aaaa",
				},
				segmento: {
					motivo: "porque esta muy bonito",
					confianza: 0.9,
					eleccion: new Segmento("500000", "segmento", []),
				},
				familia: {},
				clase: {},
				producto: {},
			};
		}),
	];
}

export async function cargarArticulosDeExcel(
	e: Event,
): Promise<Clasificacion[]> {
	const datos = await cargarExcel(e);
	return datos
		.filter((row) => !row?.id || !row?.nombre)
		.map((row) => {
			const { id, nombre, descripcion, segmento, familia, clase, producto } =
				row;
			const clasificacion: Clasificacion = {
				articulo: {
					id,
					nombre,
					descripcion,
				},
				segmento: {},
				familia: {},
				clase: {},
				producto: {},
			};
			if (segmento)
				clasificacion.segmento = {
					confianza: 1,
					eleccion: new Segmento(String(row.segmento), "segmento", []),
				};
			if (familia)
				clasificacion.familia = {
					confianza: 1,
					eleccion: new Familia(String(row.familia), "familia", []),
				};
			if (clase)
				clasificacion.clase = {
					confianza: 1,
					eleccion: new Clase(String(row.clase), "clase", []),
				};
			if (producto)
				clasificacion.producto = {
					confianza: 1,
					eleccion: new Producto(String(row.producto), "producto"),
				};
			return clasificacion;
		});
}

export async function generateDescription(
	values: Clasificacion[],
): Promise<Record<string, string>> {
	const response = await API.descripcion.generate(
		{
			pais: "",
			rubro: "",
		},
		values.map((e) => [e.articulo.id, e.articulo.nombre]),
	);
	const result = await response.json()
	console.log(result)
	return {};
}
