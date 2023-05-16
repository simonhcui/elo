import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/HomePage/TrophiesTable";
import { WinrateEloTable } from "../Components/HomePage/WinrateEloTable";

const Home = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Simon LGS Stats</h1>
      <h2 style={{ textAlign: "center" }}>Season 3 (4/6/23 - 6/29/23)</h2>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates. Last Updated 5/13/23 (Min 4 Drafts)
        {/* <p>Updated under Season 2, Season 3 about to start</p> */}
      </h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
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
