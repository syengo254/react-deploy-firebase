import './App.css';
import Counter from './components/Counter';

function App() {
  return (
    <div className="App">
      <nav>
        <a href="/">Home</a>
      </nav>
      This is react app that will be deployed to Google's Firebase hosting via Github Actions.
      <p>Enjoy!!</p>
      <Counter startCount={-1} />
    </div>
  );
}

export default App;
