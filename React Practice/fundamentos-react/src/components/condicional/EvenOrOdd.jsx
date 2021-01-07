import React from "react";

const EvenOrOdd = (props) => {
  const isEven = props.num % 2 === 0;

  return <div>{isEven ? <span>Even</span> : <span>Odd</span>}</div>;
};

export default EvenOrOdd;
