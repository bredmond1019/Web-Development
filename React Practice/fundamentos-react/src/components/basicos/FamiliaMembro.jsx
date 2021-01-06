import React from "react";

const FamiliaMembro = (props) => {
  return (
    <div>
      {props.name} <strong>{props.lastname}</strong>
    </div>
  );
};

export default FamiliaMembro;
