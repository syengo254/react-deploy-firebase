import { useState } from "react";

import './counter.css';

function Counter({ startCount = 0 }) {
    const [count, setCount] = useState(startCount);

    return (
        <div className="counter">
            <button type="button" onClick={() => setCount(count - 1)}>-</button>
            <span>{count}</span>
            <button type="button" onClick={() => setCount(count + 1)}>+</button>
        </div>
    );
}

export default Counter;
