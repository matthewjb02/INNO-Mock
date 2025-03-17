import React from "react";
import {createRoute} from "@tanstack/react-router";
import {rootRoute} from "./root.jsx";



export const homePageRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: "/",
    component: function Index() {
        return (
            <>
                <p> erurb</p>
            </>
        );
    },
});