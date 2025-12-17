---
title: Physical AI Book
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

<div className={styles.heroBanner}>
  <div className="container">
    <h1 className="hero__title">Embodied Intelligence</h1>
    <p className="hero__subtitle">The Definitive Guide to Physical AI, Robotics, and Ethics.</p>
    <div className={styles.buttons}>
      <a className={styles.startButton} href={useBaseUrl('/docs/introduction')}>
        Start Reading
      </a>
    </div>
  </div>
</div>

<div className={styles.corePillars}>
  <div className="container">
    <h2>Core Pillars</h2>
    <div className={styles.pillarsContainer}>
      <div className={styles.pillar}>
        <h3>Perception</h3>
        <p>Computer Vision, LiDAR, and SLAM technologies.</p>
      </div>
      <div className={styles.pillar}>
        <h3>Actuation</h3>
        <p>Motors, ZMP, and Humanoid Locomotion.</p>
      </div>
      <div className={styles.pillar}>
        <h3>Cognition</h3>
        <p>Ethical reasoning and decision making in the physical world.</p>
      </div>
      <div className={styles.pillar}>
        <h3>Learning & Adaptation</h3>
        <p>Machine learning, reinforcement learning, and adaptive behaviors in dynamic environments.</p>
      </div>
    </div>
  </div>
</div>

<div className={styles.section}>
  <div className="container">
    <h2>Complete Book Structure</h2>
    <div className={styles.pillarsContainer}>
      <div className={styles.pillar}>
        <h3>Chapter 1: Introduction</h3>
        <p>What is Embodied Intelligence? Why does AI need a body?</p>
      </div>
      <div className={styles.pillar}>
        <h3>Chapter 2: Sensors & Actuators</h3>
        <p>LiDAR, Cameras, IMUs (The Senses) & Motors/Servos (The Muscles).</p>
      </div>
      <div className={styles.pillar}>
        <h3>Chapter 3: Humanoid Locomotion</h3>
        <p>Zero Moment Point (ZMP), Walking Gaits, and Balance.</p>
      </div>
      <div className={styles.pillar}>
        <h3>Chapter 4: Computer Vision</h3>
        <p>Object Detection (YOLO), SLAM (Mapping), and Depth Perception.</p>
      </div>
      <div className={styles.pillar}>
        <h3>Chapter 5: Future Ethics</h3>
        <p>Robot Rights, Safety, and the "Three Laws of Robotics" in the modern age.</p>
      </div>
    </div>
  </div>
</div>

<div className={styles.section}>
  <div className="container">
    <h2>Interactive Learning</h2>
    <p>This book features an integrated chatbot that allows you to ask questions about the content in real-time. Look for the chat widget in the bottom-right corner of each page to get explanations, clarifications, and examples related to the book content.</p>
  </div>
</div>

<div className={styles.section}>
  <div className="container">
    <h2>About This Book</h2>
    <p>This interactive textbook combines traditional learning materials with AI-powered assistance to provide a personalized learning experience. Whether you're new to robotics or an experienced practitioner, this book offers insights into the current state and future potential of Physical AI.</p>
  </div>
</div>

<div className="text--center">
  <img src={useBaseUrl('img/robot-illustration.svg')} alt="Physical AI Concept" className={styles.heroImage} />
</div>

<div className={styles.nextSteps}>
  <div className="container">
    <h2>Next Steps</h2>
    <ul>
      <li><a href={useBaseUrl('/docs/introduction')}>Chapter 1: Start with Introduction to Physical AI</a></li>
      <li><a href={useBaseUrl('/docs/sensors-actuators')}>Chapter 2: Explore Sensors & Actuators</a></li>
      <li><a href={useBaseUrl('/docs/locomotion')}>Chapter 3: Understand Humanoid Locomotion</a></li>
      <li><a href={useBaseUrl('/docs/computer-vision')}>Chapter 4: Master Computer Vision</a></li>
      <li><a href={useBaseUrl('/docs/future-ethics')}>Chapter 5: Delve into Future Ethics</a></li>
    </ul>
  </div>
</div>