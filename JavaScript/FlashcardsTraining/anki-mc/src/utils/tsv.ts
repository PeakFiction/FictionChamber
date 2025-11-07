import type { Card } from "../types";

// Parse Anki-style TSV with comment/meta lines starting with "#"
export function parseTsvToCards(tsv: string, deckName: string): Card[] {
  return tsv
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .filter((line) => !line.startsWith("#")) // skip header/meta
    .map((line, idx) => {
      const [front, ...rest] = line.split("\t");
      const back = rest.join("\t"); // keep any extra tabs in the back

      return {
        id: `${deckName}-${idx}`,
        front: front ?? "",
        back: back ?? "",
      } as Card;
    })
    .filter((c) => c.front && c.back);
}

