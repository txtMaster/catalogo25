<script lang="ts">
	import {
		clasificacionToArray,
		type Clasificacion,
	} from "$lib/interfaces/IArticulo";
	import { createExcel } from "$lib/utils/excelUtils";

	let {
		clasificaciones,
	}: {
		clasificaciones: Clasificacion[] | Record<string, Clasificacion>;
	} = $props();
	function buttonHandle() {
		if (clasificaciones.length === 0) return;
        const {keys } = clasificacionToArray;
		let values: Array<any[]> = [];
		if (Array.isArray(clasificaciones)) {
			values = clasificaciones.map((c) => {
				return clasificacionToArray.exec(c);
			});
		} else {
			values = Object.values(clasificaciones).map((c) => {
				return clasificacionToArray.exec(c);
			});
		}
		createExcel([
            {size:10,title:keys[0]},
            {size:30,title:keys[1]},
            {size:50,title:keys[2]},
            {size:12,title:keys[3]},
            {size:12,title:keys[4]},
            {size:12,title:keys[5]},
            {size:12,title:keys[6]},
        ], values);
	}
</script>

<button class="borded" onclick={buttonHandle}> Descargar Resultados </button>
