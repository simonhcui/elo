import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/HomePage/TrophiesTable";
import { WinrateEloTable } from "../Components/HomePage/WinrateEloTable";

const Home = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Simon LGS Stats</h1>
      <h2 style={{ textAlign: "center" }}>Season 2</h2>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates. Last Updated 1/5/23
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
