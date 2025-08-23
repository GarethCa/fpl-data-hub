import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders welcome text', () => {
  render(<App />);
  const welcomeElement = screen.getByText(/welcome to the fantasy premier league app/i);
  expect(welcomeElement).toBeInTheDocument();
});