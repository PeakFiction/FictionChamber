export type Card = {
  id: string;
  front: string;
  back: string;
};

export type Question = {
  id: string;
  prompt: string;
  choices: string[];
  correctIndex: number;
};

