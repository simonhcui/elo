import React from "react";
import { StyleSheet, View } from "react-native";
import { WinrateEloTable } from "../Components/SeasonFour/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Season 4 (6/29/23 - 9/28/233)</h1>
      <h2 style={{ textAlign: "center" }}>
        <p>
          ELO and Winrates (Players with min 4 drafts shown, min 12 drafts to be
          in awards contention). Last Updated 9/28/23
        </p>
        <p>Winrate Champion Tony, Trophies Champion Clayton</p>
      </h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
        </View>
      </div>
    </>
  );
};

export default SeasonOne;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "space-around",
  },
});
