import { Routes, Route } from "react-router-dom";
import React from "react";
import Header from "./Header.jsx";
import BlogList from "./BlogList.jsx";
import PageNotFound from "./PageNotFound.jsx";
import BlogPost from "./BlogPost.jsx";
import SidePopup from "./SidePopup.jsx";
import WriteBlog from "./WriteBlog.jsx";

const App = () => {
  return (
    <>
      <Header />
      <SidePopup />
      <main className="w-full pt-10">
        <Routes>
          <Route
            path="/"
            element={<BlogList />}
          />

          <Route
            path="/write"
            element={<WriteBlog />} //TODO : Write only if authenticated (send user back if bad)
          />

          <Route
            path="blogs/:blogID"
            element={<BlogPost />}
          />

          <Route
            path="*"
            element={<PageNotFound />}
          />
        </Routes>
      </main>
    </>
  );
};

export default App;
