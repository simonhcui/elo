import React from "react";
import { StyleSheet, View } from "react-native";
//import { TrophiesTable } from "../Components/HomePage/TrophiesTable";
import { WinrateEloTable } from "../Components/HomePage/WinrateEloTable";

const Home = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Simon LGS Stats</h1>
      <h2 style={{ textAlign: "center" }}>Season 8 (7/2/24 - 9/26/24)</h2>
      <h2 style={{ textAlign: "center" }}>
        {/* ELO and Winrates. Last Updated 6/13/24 (Min 4 Drafts) */}
        <p>Updated under Season 7 Page, Season 8 starting soon!</p>
      </h2>
      <div>
        <View style={styles.container}>
          {/* <WinrateEloTable /> */}
          {/* <TrophiesTable /> */}
        </View>
      </div>
    </>
  );
};

export default Home;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "space-around",
  },
});
