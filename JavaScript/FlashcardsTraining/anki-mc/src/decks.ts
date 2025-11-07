import { parseTsvToCards } from "./utils/tsv";
import type { Card } from "./types";

export type Deck = {
  id: string;   // e.g. "CC_Week5_Basic2"
  name: string; // display name (same for now)
  cards: Card[];
};

// Load all .tsv under src/flashcardsTSV as raw text
const rawDecks = import.meta.glob("./flashcardsTSV/*.tsv", {
  as: "raw",
  eager: true,
}) as Record<string, string>;

export const decks: Deck[] = Object.entries(rawDecks).map(([path, content]) => {
  // path like "./flashcardsTSV/CC_Week5_Basic2.tsv"
  const match = path.match(/\/([^/]+)\.tsv$/);
  const deckName = match ? match[1] : path;
  const cards = parseTsvToCards(content, deckName);

  return {
    id: deckName,
    name: deckName,
    cards,
  };
});

