import React from 'react';
import ReactDOM from 'react-dom';
import CommentDetail from "./CommentDetail";
import faker from 'faker';

const App = () => {
    return (
        <div className="ui container comments">
            <CommentDetail author="Sam"  timeAgo="Today at 4:45PM" profilePic={faker.image.image()} comment="Awesome!"/>
            <CommentDetail author="Jane" timeAgo="Today at 2:00AM" profilePic={faker.image.image()} comment="Thanks, dude. Appreciate you!"/>
            <CommentDetail author="Alex" timeAgo="Yesterday at 1:45PM" profilePic={faker.image.image()} comment="Hahahaha"/>
        </div>
    )
};

ReactDOM.render(<App />, document.querySelector('#root'));


