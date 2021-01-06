import React from "react";

const Familia = (props) => {
  return (
    <div>
      {React.Children.map(props.children, (child) => {
        return React.cloneElement(child, props);
      })}
    </div>
  );
};

export default Familia;
