import { useEffect, useState } from "react";

function Visualizer() {
  const [bars, setBars] = useState(Array(40).fill(10));

  useEffect(() => {
    const interval = setInterval(() => {
      setBars(bars.map(() => Math.floor(Math.random() * 60) + 10));
    }, 100);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="visualizer">
      {bars.map((height, index) => (
        <div
          key={index}
          className="bar"
          style={{ height: `${height}px` }}
        ></div>
      ))}
    </div>
  );
}

export default Visualizer;
