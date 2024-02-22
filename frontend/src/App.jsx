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
      <p>{process.env.REACT_APP_TEST_VAR}</p>
    </div>
  );
}

export default App;
