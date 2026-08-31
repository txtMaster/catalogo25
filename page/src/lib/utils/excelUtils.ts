import * as XLSX from "xlsx";
export async function createExcel(
	headers: { size: number; title: string }[],
	values: Array<any[]>,
) {
	const sizes = headers.map((e) => ({ wch: e.size }));
	const titles = headers.map((e) => e.title);
	const worksheet = XLSX.utils.aoa_to_sheet([titles, ...values]);
	worksheet["!cols"] = sizes;
	const workbook = XLSX.utils.book_new();
	XLSX.utils.book_append_sheet(workbook, worksheet, "Articulos");
	XLSX.writeFile(workbook, "excel.xlsx");
}
