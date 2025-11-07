import type { Card, Question } from "../types";

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function buildQuestionsFromCards(
  cards: Card[],
  choicesPerQuestion = 4
): Question[] {
  if (cards.length === 0) return [];

  return cards.map((card, idx) => {
    const others = cards.filter((_, i) => i !== idx);
    const nChoices = Math.min(choicesPerQuestion - 1, others.length);

    const shuffledOthers = shuffle(others);
    const distractors = shuffledOthers.slice(0, nChoices).map((c) => c.back);

    const allChoices = shuffle([card.back, ...distractors]);
    const correctIndex = allChoices.indexOf(card.back);

    return {
      id: card.id,
      prompt: card.front,
      choices: allChoices,
      correctIndex,
    } as Question;
  });
}
