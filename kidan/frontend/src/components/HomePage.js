import React, {Component} from "react";
import CreateAccountPage from "./CreateAccountPage";
import ProfilePage from "./ProfilePage";
import {
    BrowserRouter as Router,
    Routes,
    Route, 
    Link, 
    Redirect
} from "react-router-dom"

export default class HomePage extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <Router>
            <Routes>
                <Route path="/" element={<h1>This is the HomePage</h1>}/>
                <Route path="/register" element={<CreateAccountPage/>}/>
                <Route path="/profile" element={<ProfilePage/>}/>
            </Routes>
        </Router>
    }
}