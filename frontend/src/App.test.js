import { render, screen } from '@testing-library/react';
import App from './App';

test('renders home page', () => {
  render(<App />);
  const text = screen.getByText(/will be deployed to Google's Firebase/i);
  expect(text).toBeInTheDocument();
});
