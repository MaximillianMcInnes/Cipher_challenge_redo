// components/CubeLoader.tsx

import React from 'react';
import styles from './CubeLoader.module.css'; // Import the CSS module

const CubeLoader = () => {
  return (
    <div className={styles.container}>
      <div className={styles.cube}>
        <div className={styles.cube__inner}></div>
      </div>
      <div className={styles.cube}>
        <div className={styles.cube__inner}></div>
      </div>
      <div className={styles.cube}>
        <div className={styles.cube__inner}></div>
      </div>
    </div>
  );
};

export default CubeLoader;
