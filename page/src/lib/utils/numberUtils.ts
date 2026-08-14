export function floatToPercentage(number: number): string {
	return `${Math.round(Math.abs(number * 100))}%`;
}
