import React from "react";
import { StyleSheet, View } from "react-native";

const ModernHorizonsOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Modern Horizons 1 Stats (3 Drafts Total)
      </h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 12/9/22
      </h2>
      <h2 style={{ textAlign: "center" }}>TBD once more data is collected</h2>
      <div>
        <View style={styles.container}>
          {/* <ColorTable />
          <Table />
          <WinrateTable />
          <EloTable />
          <TrophiesTable /> */}
        </View>
      </div>
    </>
  );
};

export default ModernHorizonsOne;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "center",
  },
});
