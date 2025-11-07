import { useMemo, useState } from "react";
import { decks } from "./decks";
import { buildQuestionsFromCards } from "./utils/questions";
import type { Question } from "./types";
import "./App.css";

function App() {
  const [deckId, setDeckId] = useState(decks[0]?.id ?? "");
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [answeredCount, setAnsweredCount] = useState(0);

  const currentDeck = useMemo(
    () => decks.find((d) => d.id === deckId),
    [deckId]
  );

  const questions: Question[] = useMemo(() => {
    if (!currentDeck) return [];
    return buildQuestionsFromCards(currentDeck.cards, 4);
  }, [currentDeck]);

  const currentQuestion = questions[currentIndex];

  const handleSelectDeck = (id: string) => {
    setDeckId(id);
    setCurrentIndex(0);
    setSelectedIndex(null);
    setShowAnswer(false);
    setCorrectCount(0);
    setAnsweredCount(0);
  };

  const handleChoiceClick = (idx: number) => {
    if (!currentQuestion) return;
    if (showAnswer) return;

    setSelectedIndex(idx);
    setShowAnswer(true);
    setAnsweredCount((c) => c + 1);
    if (idx === currentQuestion.correctIndex) {
      setCorrectCount((c) => c + 1);
    }
  };

  const handleNext = () => {
    if (!questions.length) return;
    const nextIndex = (currentIndex + 1) % questions.length;
    setCurrentIndex(nextIndex);
    setSelectedIndex(null);
    setShowAnswer(false);
  };

  if (!currentDeck || !currentQuestion) {
    return <div className="app-root">No decks / questions found.</div>;
  }

  const accuracy =
    answeredCount === 0 ? 0 : Math.round((100 * correctCount) / answeredCount);

  return (
    <div className="app-root">
      <div className="app-inner">
        <h1 className="app-title">Anki TSV MC Trainer</h1>

        <div className="top-row">
          <div className="deck-select">
            <label>
              Deck:
              <select
                value={deckId}
                onChange={(e) => handleSelectDeck(e.target.value)}
              >
                {decks.map((d) => (
                  <option key={d.id} value={d.id}>
                    {d.name} ({d.cards.length} cards)
                  </option>
                ))}
              </select>
            </label>
          </div>

          <div className="stats">
            Q {currentIndex + 1}/{questions.length} | Correct {correctCount}/
            {answeredCount} ({accuracy}%)
          </div>
        </div>

        <div className="question">
          <h2>{currentQuestion.prompt}</h2>
        </div>

        <div className="choices">
          {currentQuestion.choices.map((choice, idx) => {
            const isCorrect = idx === currentQuestion.correctIndex;
            const isSelected = idx === selectedIndex;

            let state = "base";
            if (showAnswer && isCorrect && isSelected) state = "correct-selected";
            else if (showAnswer && isCorrect) state = "correct";
            else if (showAnswer && isSelected && !isCorrect)
              state = "incorrect-selected";

            const className = `choice-button choice--${state}`;

            return (
              <button
                key={idx}
                className={className}
                onClick={() => handleChoiceClick(idx)}
              >
                {choice}
              </button>
            );
          })}
        </div>

        <div className="controls">
          <button className="next-button" onClick={handleNext}>
            Next
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
