import React from "react";
import { StyleSheet, View } from "react-native";
import { WinrateEloTable } from "../Components/SeasonSix/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Season 6 (1/4/24 - 3/28/24)</h1>
      <h2 style={{ textAlign: "center" }}>
        <p>
          ELO and Winrates (Players with min 4 drafts shown, min 12 drafts to be
          in awards contention). Last Updated 3/28/24
        </p>
        <p>Winrate Champion and Trophies Champion Alberto M</p>
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
