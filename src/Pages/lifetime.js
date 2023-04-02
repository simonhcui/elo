import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/Lifetime/TrophiesTable";
import { AchievementsTable } from "../Components/HomePage/AchievementsTable";
import { WinrateEloTable } from "../Components/Lifetime/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Lifetime Stats</h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 3/30/22. Updated at end of
        season.
      </h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
          <AchievementsTable />
          {/* <TrophiesTable /> */}
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
